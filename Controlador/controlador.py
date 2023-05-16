import websocket
import threading
import json
import requests

from Modelo.modelo import modelo_tablero
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal, QMetaObject

class Controlador(object):
    def __init__(self, modelo: modelo_tablero, vista, username, num_jug, tipo, codigo):
        self.modelo = modelo
        self.vista = vista
        self.username = username
        self.num_jugadores = num_jug
        self.tipo = tipo
        self.codigo = codigo
        self.sala_espera = True
        self.direccion_socket_chat = "wss://guinote-unizar.onrender.com/ws/"
        threading.Thread(target=self.iniciarSocket).start()


    def formatear_cartas(self, cartasSinFormato):
        cartasFormateadas = []
        for carta in cartasSinFormato:
            cartaFormateada = carta[0] + "-" + str(carta[1])
            cartasFormateadas.append(cartaFormateada)
        return cartasFormateadas
    
    def jugar_carta(self, posicion):
        carta = self.modelo.get_carta(posicion)
        self.ws.send(carta)

    def cambiar7(self, decision):
        self.ws.send(decision)
        
    def on_open(self, ws):
        print("Conexión creada")

    def gestor_mensajes(self, ws, message):
        try:
            mensaje = json.loads(message)  # Decodificar el mensaje JSON
        except:
            mensaje = message

        if "Cartas" in mensaje:
            cartas = self.formatear_cartas(mensaje["Cartas"])
            self.modelo.set_mano(cartas)
            self.vista.rellenarMiMano(self.modelo)
            self.modelo.set_cartas_posibles(cartas)
            self.vista.set_cartas_posibles(self.modelo)
            
        if "Cartas Posibles" in mensaje:
            cartas = self.formatear_cartas(mensaje["Cartas Posibles"])
            print(cartas)
            self.modelo.set_cartas_posibles(cartas)
            self.vista.set_cartas_posibles(self.modelo)

        if "Triunfo" in mensaje:
            triunfo = mensaje["Triunfo"]
            if triunfo != None:
                self.modelo.set_triunfo(triunfo[0] + "-" + str(triunfo[1]))
                self.vista.mostrarTriunfo(self.modelo)

        if "Turno" in mensaje:
            print("x")
            if self.num_jugador == mensaje["Turno"]:
                self.vista.puede_jugar(True, None)
            else:
                self.vista.puede_jugar(False, None)

        if "0" in mensaje:
            if not self.sala_espera: 
                #Carta jugador 1
                carta = mensaje["0"]
                if carta != None and type(carta) != int:
                    self.modelo.set_carta_jugada(0,carta[0] + "-" + str(carta[1]))
                else:
                    self.modelo.set_carta_jugada(0, "")

                #Carta jugador 2
                carta = mensaje["1"]
                if carta != None and type(carta) != int:
                    self.modelo.set_carta_jugada(1,carta[0] + "-" + str(carta[1]))
                else:
                    self.modelo.set_carta_jugada(1, "")

                #Carta jugador 3
                if "2" in mensaje:
                    carta = mensaje["2"]
                    if carta != None and type(carta) != int:
                        self.modelo.set_carta_jugada(2,carta[0] + "-" + str(carta[1]))
                    else:
                        self.modelo.set_carta_jugada(2, "")

                #Carta jugador 4
                if "3" in mensaje:
                    carta = mensaje["3"]
                    if carta != None and type(carta) != int:
                        self.modelo.set_carta_jugada(3,carta[0] + "-" + str(carta[1]))
                    else:
                        self.modelo.set_carta_jugada(3, "")

                
                #Mostrar cartas en la vista
                self.vista.mostrar_cartas_jugadas(self.modelo, self.num_jugador)

            else:
                jugador0 = mensaje["0"]
                if jugador0 == self.username:
                    self.num_jugador = 0

                jugador1 = mensaje["1"]
                if jugador1 == self.username:
                    self.num_jugador = 1

                if "2" in mensaje:
                    jugador2 = mensaje["2"]
                    if jugador2 == self.username:
                        self.num_jugador = 2
                else:
                    jugador2 = None

                if "3" in mensaje:
                    jugador3 = mensaje["3"]
                    if jugador3 == self.username:
                        self.num_jugador = 3
                else:
                    jugador3 = None

                self.modelo.set_jugadores(jugador0, jugador1, jugador2, jugador3)
                self.vista.mostrar_jugadores_sala_espera(self.modelo)
                self.vista.mostrar_nombres_jugadores(self.modelo, self.num_jugador)

        if "Ganador Partida" in mensaje:
            self.cerrar_websockets()
            ganador = mensaje["Ganador Partida"]
            if self.num_jugadores != 4:
                if ganador == self.num_jugador:
                    self.vista.ganador_partida(True)
                else:
                    self.vista.ganador_partida(False)
            else:
                if self.num_jugador in ganador:
                    self.vista.ganador_partida(True)
                else:
                    self.vista.ganador_partida(False)

        if "chat" in mensaje:
            idChat = mensaje["chat"]
            print("AA")
            self.direccion_socket_chat += (idChat + "/" + self.username)
            print("AA")
            print(self.direccion_socket_chat)
            threading.Thread(target=self.iniciar_socket_chat).start()

        if "Cambiar7" in mensaje:
            puede = mensaje["Cambiar7"]
            if puede:
                self.vista.puede_cambiar()


        if "Comienza partida" == mensaje:
            self.sala_espera = False
            self.vista.pantalla_tablero()

        if "Arrastre"  == mensaje:
            self.vista.arrastre()

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("Conexión cerrada")

    def iniciarSocket(self):
        #websocket.enableTrace(True)
        if self.tipo == "publica":
            #"wss://guinote-unizar.onrender.com/partida" + str(self.num_jugadores) + "/" + self.username
            #"wss://guinote-unizar.onreder.com/partidaIA/" + self.username
            self.ws = websocket.WebSocketApp("wss://guinote-unizar.onrender.com/partidaIA/" + self.username,
                                        on_open=self.on_open,
                                        on_message=self.gestor_mensajes,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
            self.num_jugador = 0
        
        if self.tipo == "privada":
            if self.codigo == "crear":
                response = requests.post("https://guinote-unizar.onrender.com/crear/partida" + str(self.num_jugadores))
                response_parsed = response.json()
                self.vista.mostrar_codigo(response_parsed["codigo"])
                self.codigo = response_parsed["codigo"]

            self.ws = websocket.WebSocketApp("wss://guinote-unizar.onrender.com/partida" + str(self.num_jugadores) + "/join/" + self.username + "/" + self.codigo,
                                        on_open=self.on_open,
                                        on_message=self.gestor_mensajes,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        
        self.ws.run_forever()


    def gestor_mensajes_chat(self, ws, message):
        try:
            mensaje = json.loads(message)
            if "username" in mensaje:
                mensaje_usuario = mensaje["username"]
                mensaje_texto = mensaje["message"]
                self.vista.mostrar_mensaje(mensaje_usuario, mensaje_texto)
        except:
            self.vista.mostrar_mensaje(None, message)

    def enviar_mensaje_chat(self, mensaje):
        try:
            message = json.dumps(mensaje)
            self.ws_chat.send(message)
        except:
            pass

    def iniciar_socket_chat(self):
        self.ws_chat = websocket.WebSocketApp(self.direccion_socket_chat,
                                              on_open=self.on_open,
                                              on_message=self.gestor_mensajes_chat,
                                              on_error=self.on_error,
                                              on_close=self.on_close)
        self.ws_chat.run_forever()
    
    def cerrar_websockets(self):
        self.ws.close()
        self.ws_chat.close()
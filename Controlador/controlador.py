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
        msj = self.modelo.devolver_jugador(self.num_jugador) + " ha cambiado el 7"
        self.vista.mostrar_cante(msj)
        
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
                print("siu")
                self.modelo.set_triunfo(triunfo[0] + "-" + str(triunfo[1]))
                self.vista.mostrarTriunfo(self.modelo)

        if "Turno" in mensaje:
            print("x")
            if self.num_jugador == mensaje["Turno"]:
                self.vista.puede_jugar(True, None)
            else:
                self.vista.puede_jugar(False, None)

        # if "Ganador" in mensaje:
        #     self.vista.mostrar_ganador_baza(self.modelo.devolver_jugador(mensaje["Ganador"]))

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
            ptsRival1 = None
            ganador = mensaje["Ganador Partida"]
            ptsMios = mensaje[str(self.num_jugador)]
            if self.num_jugadores == 2:
                if self.num_jugador == 0:
                    ptsRival = mensaje["1"]
                else:
                    ptsRival = mensaje["0"]
            elif self.num_jugadores == 3:
                if self.num_jugador == 0:
                    ptsRival1 = mensaje["1"]
                    ptsRival2 = mensaje["2"]
                elif self.num_jugador == 1:
                    ptsRival1 = mensaje["2"]
                    ptsRival2 = mensaje["0"]
                else:
                    ptsRival1 = mensaje["0"]
                    ptsRival2 = mensaje["1"]
            else:
                if self.num_jugador == 0 or self.num_jugador == 2:
                    ptsRival = mensaje["1"]
                else:
                    ptsRival = mensaje["0"]

            if ptsRival1 == None:
                if ptsMios > ptsRival:
                    ptosGanador = ptsMios
                else:
                    ptosGanador = ptsRival
            else:
                if ptsMios > ptsRival1 and ptsMios > ptsRival2:
                    ptosGanador = ptsMios
                elif ptsRival1 > ptsRival2:
                    ptosGanador = ptsRival1
                else:
                    ptosGanador = ptsRival2

            if ganador != None:
                if self.num_jugadores != 4:
                    msg = "Ganador de la partida " + self.modelo.devolver_jugador(ganador) + " con " + str(ptosGanador) + " puntos"
                else:
                    msg = "Ganadores de la partida " + self.modelo.devolver_jugador(ganador[0]) + " y \n" + self.modelo.devolver_jugador(ganador[1]) + " con " + str(ptosGanador) + " puntos"
            else:
                if self.num_jugadores != 3:
                    msg = "Tus puntos: " + str(ptsMios) + ", Puntos rival: " + str(ptsRival)
                else:
                    msg = "Tus puntos: " + str(ptsMios) + ", Puntos rival 1: " + str(ptsRival1) + ", Puntos rival 2: " + str(ptsRival2)
            self.vista.mostrar_cante(msg)

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

        if "Canta" in mensaje:
            puntos = mensaje["Canta"]
            palo = mensaje["Palo"]
            jug = self.modelo.devolver_jugador(mensaje["Jugador"])
            msg = jug + " canta " + str(puntos) + " en " + palo
            self.vista.mostrar_cante(msg)


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
            #"wss://guinote-unizar.onrender.com/partidaIA/" + self.username
            self.ws = websocket.WebSocketApp("wss://guinote-unizar.onrender.com/partida" + str(self.num_jugadores) + "/" + self.username,
                                        on_open=self.on_open,
                                        on_message=self.gestor_mensajes,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        
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
        
        if self.tipo == "ia":
            self.ws = websocket.WebSocketApp("wss://guinote-unizar.onrender.com/partidaIA/" + self.username,
                                        on_open=self.on_open,
                                        on_message=self.gestor_mensajes,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
            self.num_jugador = 0
            self.modelo.set_jugadores(self.username, "IA-1", "IA-2", "IA-3")
            self.vista.mostrar_nombres_jugadores(self.modelo, self.num_jugador)

        
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
            while '"' in message:
                message = message.replace('"', '')
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
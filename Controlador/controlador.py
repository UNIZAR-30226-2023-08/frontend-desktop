import asyncio
import websocket
import threading
import time
import json
from Modelo.modelo import modelo_tablero

class Controlador(object):
    def __init__(self, modelo: modelo_tablero, vista, username):
        self.modelo = modelo
        self.vista = vista
        self.username = username
        threading.Thread(target=self.iniciarSocket).start()
        
    def on_open(self, ws):
        print("Conexión creada")

    def gestor_mensajes(self, ws, message):
        mensaje = json.loads(message)  # Decodificar el mensaje JSON
        
        if "Jugador" in mensaje:
            self.num_jugador = mensaje["Jugador"]

        if "Cartas" in mensaje:
            cartas = self.formatear_cartas(mensaje["Cartas"])
            self.modelo.set_mano(cartas)
            self.vista.rellenarMiMano(self.modelo)

        if "Triunfo" in mensaje:
            triunfo = mensaje["Triunfo"]
            self.modelo.set_triunfo(triunfo[0] + "-" + str(triunfo[1]))
            self.vista.mostrarTriunfo(self.modelo)

        if "Turno" in mensaje:
            if self.num_jugador == mensaje["Turno"]:
                self.vista.puede_jugar(True)
            else:
                self.vista.puede_jugar(False)

        if "0" in mensaje:
            #Carta jugador 1
            carta = mensaje["0"]
            if carta != None:
                self.modelo.set_carta_jugada(0,carta[0] + "-" + str(carta[1]))
            else:
                self.modelo.set_carta_jugada(0, "no_hay_foto")
            #Carta jugador 2
            carta = mensaje["1"]
            if carta != None:
                self.modelo.set_carta_jugada(1,carta[0] + "-" + str(carta[1]))
            else:
                self.modelo.set_carta_jugada(1, "no_hay_foto")
            
            self.vista.mostrar_cartas_jugadas(self.modelo, self.num_jugador)

        if "Ganador" in mensaje:
            time.sleep(3)
        
    
    def prueba_rellenar(self):
        self.modelo.set_mano(['oro-12', 'oro-4', 'copa-3', 'copa-7', 'basto-1', 'espada-5'])
        self.vista.rellenarMiMano(self.modelo)
            

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("Conexión cerrada")

    def iniciarSocket(self):
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:8000/partida2/" + self.username,
                                    on_open=self.on_open,
                                    on_message=self.gestor_mensajes,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.ws.run_forever()

    def formatear_cartas(self, cartasSinFormato):
        cartasFormateadas = []
        for carta in cartasSinFormato:
            cartaFormateada = carta[0] + "-" + str(carta[1])
            cartasFormateadas.append(cartaFormateada)
        return cartasFormateadas
    
    def jugar_carta(self, posicion):
        carta = self.modelo.get_carta(posicion)
        self.ws.send(carta)
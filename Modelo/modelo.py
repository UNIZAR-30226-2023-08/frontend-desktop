class modelo_tablero:
    def __init__(self):
        self.cartas_jugadas = [None, None, None, None]
        self.mis_cartas = [None, None, None, None, None, None]
        self.cartas_posibles = []
        self.carta_triunfo = None
        self.num_jugador = 0
        self.jugador0 = "Esperando..."
        self.jugador1 = "Esperando..."
        self.jugador2 = "Esperando..."
        self.jugador3 = "Esperando..."

    def set_mano(self, cartas):
        if len(cartas) == len(self.mis_cartas):    
            self.mis_cartas = cartas
            self.mis_cartas.sort()
        else:
            for i in range(len(cartas)):
                self.mis_cartas[i] = cartas[i]

            for j in range(i+1,6):
                self.mis_cartas[j] = ""
        self.set_cartas_posibles(cartas)

    def set_cartas_posibles(self, cartas):
        self.cartas_posibles = cartas

    def get_num_cartas_posibles(self):
        num_cartas_posibles = []
        for carta_posible in self.cartas_posibles:
            if carta_posible in self.mis_cartas:
                i = self.mis_cartas.index(carta_posible)
                num_cartas_posibles.append(i)
        return num_cartas_posibles

    def set_triunfo(self, carta):
        self.carta_triunfo = carta

    def get_carta(self, posicion):
        return self.mis_cartas[posicion]
    
    def set_carta_jugada(self, jugador, carta):
        if jugador == 0:
            self.cartas_jugadas[0] = carta
        elif jugador == 1:
            self.cartas_jugadas[1] = carta
        elif jugador == 2:
            self.cartas_jugadas[2] = carta
        else:
            self.cartas_jugadas[3] = carta

    def set_jugadores(self, jugador0, jugador1, jugador2, jugador3):
        self.jugador0 = jugador0
        if jugador1 != None:
            self.jugador1 = jugador1
        if jugador2 != None:
            self.jugador2 = jugador2
        if jugador3 != None:
            self.jugador3 = jugador3
        

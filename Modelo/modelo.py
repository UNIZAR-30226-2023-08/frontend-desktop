class modelo_tablero:
    def __init__(self):
        self.cartas_jugadas = [None, None]
        self.mis_cartas = [None, None, None, None, None, None]
        self.cartas_posibles = []
        self.carta_triunfo = None
        self.num_jugador = 0
        self.jugador0 = "Jugador 1"
        self.jugador1 = "Jugador 2"

    def set_mano(self, cartas):
        if len(cartas) == len(self.mis_cartas):    
            self.mis_cartas = cartas
            self.mis_cartas.sort()
        else:
            for i in range(len(cartas)):
                self.mis_cartas[i] = cartas[i]

            for j in range(i+1,6):
                self.mis_cartas[j] = "vacia"

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
        else:
            self.cartas_jugadas[1] = carta

    def set_jugadores(self, jugador0, jugador1):
        self.jugador0 = jugador0
        if jugador1 != None:
            self.jugador1 = jugador1

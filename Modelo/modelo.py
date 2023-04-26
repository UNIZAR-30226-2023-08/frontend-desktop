class modelo_tablero:
    def __init__(self):
        self.cartas_jugadas = [None, None]
        self.mis_cartas = [None, None, None, None, None, None]
        self.carta_triunfo = None
        self.num_jugador = 0

    def set_mano(self, cartas):
        self.mis_cartas = cartas
        self.mis_cartas.sort()
    
    def set_triunfo(self, carta):
        self.carta_triunfo = carta

    def get_carta(self, posicion):
        return self.mis_cartas[posicion]
    
    def set_carta_jugada(self, jugador, carta):
        if jugador == 0:
            self.cartas_jugadas[0] = carta
        else:
            self.cartas_jugadas[1] = carta

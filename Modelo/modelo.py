class modelo_tablero:

    def set_mano(self, cartas):
        self.mis_cartas = cartas
        self.mis_cartas.sort()
    
    def set_triunfo(self, carta):
        self.carta_triunfo = carta

    def get_carta(self, posicion):
        return self.mis_cartas[posicion]

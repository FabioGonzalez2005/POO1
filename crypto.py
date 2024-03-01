class Crypto:
    def __init__(self, nombre:str, euros:float):
        self.nombre = nombre
        self.euros = euros
        self.min = 0.
        self.max = 0.

    def stopLoss(self, min:float, max:float):
        self.min = min
        self.max = max

    def imprimir(self):
        print("El valor de", self.nombre, "es", self.euros)
        print ("Stop Loss. Min:", self.min, "Stop Loss. Max:", self.max)

if __name__ == "__main__":
    bitcoin = Crypto("Bitcoin", 57000)
    bitcoin.stopLoss(55000, 60000)
    bitcoin.imprimir()
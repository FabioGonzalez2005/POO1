class Calculo:
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2
        self.suma = 0
        self.resta = 0
        self.multiplicacion = 0
        self.division = 0

    def sumaOperar(self):
        self.suma = self.numero1 + self.numero2
        return self.suma

    def restaOperar(self):
        self.resta = self.numero1 - self.numero2


    def multiplicacionOperar(self):
        self.multiplicacion = self.numero1 * self.numero2

    def divisionOperar(self):
        self.division = self.numero1 / self.numero2

    def imprimir(self):
        print("Resultado suma:", self.suma, "\nResultado resta:", self.resta, "\nResultado multiplicación:", self.multiplicacion, "\nResultado división:", self.division)

if __name__ == "__main__":
    calculo = Calculo(4, 5)
    calculo.sumaOperar()
    calculo.restaOperar()
    calculo.multiplicacionOperar()
    calculo.divisionOperar()
    calculo.imprimir()
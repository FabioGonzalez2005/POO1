class persona:
    def __init__(self, nombre, anos):
        self.nombre = nombre
        self.anos = anos

    def imprimir(self):
        print (self.nombre,"cumplió años, ahora tiene:")

    def cumpleanos(self):
        self.anos += 1
        print (self.anos)

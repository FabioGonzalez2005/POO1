class alumno:
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre

    def imprimir(self):
        print (self.nombre,"obtiene:", self.nota)

    def promociona(self):
        if self.nota >= 5:
            print("Promociona.")
        else:
            print("No promociona.")

if __name__ == "__main__":
    main()
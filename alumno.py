class alumno:
    def __init__(self):
        self.nota = 0
        self.nombre = ""

    def imprimir(self):
        print (self.nombre,"obtiene:", self.nota)

    def promociona(self):
        if self.nota >= 5:
            print("Promociona.")
        else:
            print("No promociona.")

if __name__ == "__main__":
    main()
class alumno:
    nota = 0

    def imprimir(self):
        if self.nota >= 5:
            print("Promociona.")
        else:
            print("No promociona.")

def main():
    javier = alumno()
    javier.nota = 6
    javier.imprimir()

    diego = alumno()
    diego.nota = 3
    diego.imprimir()

if __name__ == "__main__":
    main()
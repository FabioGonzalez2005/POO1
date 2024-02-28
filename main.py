from alumno import alumno

def main():
    javier = alumno()
    javier.nota = 6
    javier.imprimir()
    javier.promociona()

    diego = alumno()
    diego.nota = 3
    diego.imprimir()
    diego.promociona()

if __name__ == "__main__":
    main()
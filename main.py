from alumno import alumno

def main():
    javier = alumno("Javier", 6)
    javier.imprimir()
    javier.promociona()

    diego = alumno("Diego", 3)
    diego.imprimir()
    diego.promociona()

if __name__ == "__main__":
    main()
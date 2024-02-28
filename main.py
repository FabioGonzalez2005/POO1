from persona import persona

def main():
    javier = persona("Javier", 6)
    javier.imprimir()
    javier.cumpleanos()

    diego = persona("Diego", 17)
    diego.imprimir()
    diego.cumpleanos()

if __name__ == "__main__":
    main()
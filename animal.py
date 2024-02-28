class animal:
    patas = 0

    def caminar(self):
        self.patas = 0
        print("caminando con", self.patas, "patas")

def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()

    pato = animal()
    pato.patas = 2
    pato.caminar

    vaca.caminar()

if __name__ == "__main__":
    main()
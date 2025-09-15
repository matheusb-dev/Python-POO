class Ninja:
    def __init__(self, nNinja, nJuts):
        self.nNinja = nNinja
        self.nJutsu = nJuts

    def exibir(self):
        print(self.nJutsu, self.nNinja)
    
naruto = Ninja("naruto", "Clones das sombras")

naruto.exibir()
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}")

p = Pessoa("Matheus")
p.apresentar()
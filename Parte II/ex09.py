## Crie uma classe Aluno com os atributos nome e notas (lista de notas). 
## Crie um método que calcule a média das notas do aluno. 
## Crie um método que verifique se o aluno foi aprovado (média ≥ 7). 

class Aluno:
    def __init__(self, nome, notas): ##public
        self.nome = nome
        self.notas = notas

    def calcular_media(self):

        if not self.notas:

            return 0

        return sum(self.notas) / len(self.notas)
    

    def esta_aprovado(self):

        return self.calcular_media() >=7
    
aluno1 = Aluno("Matheus", [8.5, 4.9, 6.7])
print(f"Aluno/a {aluno1.nome}")
if aluno1.esta_aprovado():

    print("Sim! está aprovado")
else:
    print("Não! está aprovado")

aluno2 = Aluno("Otavio", [9.5, 6.5, 5.9])
print(f"Aluno/a {aluno2.nome}")
if aluno2.esta_aprovado():

    print("Sim! está aprovado")
else:
    print("Não! está aprovado")
        


    
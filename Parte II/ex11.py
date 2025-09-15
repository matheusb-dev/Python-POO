#Na classe Matematica, crie um método estático que receba um número e retorne True se 
# for primo e False caso contrário. 
#Sugestão de teste: testar com alguns números.
#

class Matematica:


    @staticmethod
    def numero_primo(num):
        if num < 2:
            return False
            
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

print(Matematica.numero_primo(7))    # Should print: True
print(Matematica.numero_primo(4))    # Should print: False
print(Matematica.numero_primo(13))   # Should print: True
print(Matematica.numero_primo(1))    # Should print: False
print(Matematica.numero_primo(25))   # Should print: False



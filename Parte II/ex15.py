class Mensagem:
    def __init__(self, remetente):

        self.remetente = remetente

    def enviar(self, texto=None, numero=None, destinatario=""):
        
        if texto is not None:
            print(f"De: {self.remetente} para {destinatario}: {texto}")
        elif numero is not None:
            print(f"De: {self.remetente} para {destinatario}: {numero}")
        else:
            print("Erro: Nenhum conteúdo de mensagem (texto ou número) foi fornecido.")


print("--- Testando com texto ---")
mensagem_texto = Mensagem("Alice")
mensagem_texto.enviar(texto="Olá, como você está?", destinatario="Bob")

print("\n--- Testando com número ---")
mensagem_numero = Mensagem("Charlie")
mensagem_numero.enviar(numero=12345, destinatario="David")
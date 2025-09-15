class Seguranca:
    def __init__(self, msg_protect):

        self._mensagem = msg_protect

    def _criptografar_mensagem(self):
        return f"Mensagem criptografada: {self._mensagem}"

    def exibir_frase_criptografada(self):
        frase = self._criptografar_mensagem()
        print(frase)

seguranca = Seguranca("Olá mundo!")
seguranca.exibir_frase_criptografada()
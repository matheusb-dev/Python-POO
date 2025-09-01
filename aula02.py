class item:
    def __init__(self, nome):
        self._nome = nome #protegido

p = item("Tenis")
print(p._nome)
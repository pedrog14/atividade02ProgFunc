class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self, peso=None, altura=None):
        peso = peso if peso is not None else self.peso
        altura = altura if altura is not None else self.altura
        return peso / (altura**2)


p1 = Pessoa("João", 65, 1.72)

print(f"O IMC de {p1.nome} é {p1.imc()}.")

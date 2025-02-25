class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self, peso=None, altura=None):
        peso = peso if peso is not None else self.peso
        altura = altura if altura is not None else self.altura

        return peso / (altura**2)


def filtroPar(a):
    return [i for i in filter(lambda b: b % 2 == 0, a)]


def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 2) + fibonacci(n - 1)


n = int(
    input(
        "Fibonacci - Insira o tamanho da lista da sequência de Fibonacci à ser gerada: "
    )
)

fib = [fibonacci(i) for i in range(n)]

print(
    f"Lista dos {n} primeiros valores da sequência de Fibonacci: {fib}",
    f"Lista dos elementos pares da sequência: {filtroPar(fib)}",
)

p1 = Pessoa("Pedro", 82, 1.67)

print(f"IMC de {p1.nome} é {p1.imc()}.")

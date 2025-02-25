# Programação Funcional - AV 2 - Python

## Aluno

Pedro Gabriel de Morais Ribeiro

## Matrícula

471550

# Introdução

Python é uma linguagem de programação de uso geral de alto nível e multiparadigma, lançada em 1991 por Guido van Rossum como sucessora da linguagem ABC. Atualmente, a linguagem é mantida pela Python Software Foundation, e se apresenta como uma das linguagens de programação mais populares da atualidade.

## Objetivos

Inicialmente proposta como sucessora à linguagem ABC, a linguagem Python atualmente apresenta-se como uma linguagem de uso geral (GPL) e com foco em sua legibilidade pelo uso de indentação como método de separação de blocos de código.

# Motivação

A concepção da linguagem realizou-se no final da década de 80, por Guido van Rossum no Centrum Wiskunde & Informatica (CWI; Português: Centro de Matemática e Ciência da Computação), Países Baixos, como sucessora à linguagem ABC, e tendo seu nome inspirado em um antigo programa de comédia britânico, Monty Python's Flying Circus.

# Caracteristicas

A linguagem Python apresenta-se como uma linguagem multiparadigma, com foco nos paradigmas de Orientação à Objetos e Programação Estruturada, mas também abrangendo recursos de paradigma Funcional e Orientado à Aspectos, além de ter sido desenvolvida com o intuito de ser uma linguagem altamente extensível através do uso de módulos.

Suas variáveis são de tipagem dinâmica, e há a implementação de um coletor de lixo de memória em seu interpretador.

A linguagem também apresenta características de linguagens de paradigma Funcional Lisp, como a presença de funções de manipulação de listas (como `filter`, `map` e `reduce`), compreensão de listas, dicionários, sets e geradores. Sua biblioteca padrão contém dois módulos (`itertools` e `functools`) que implementam funcionalidades tomadas de linguagens funcionais como Haskell e SML.

# Exemplos

## Classes e Objetos (Paradigma OO)

```python
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
```

## Cálculo Lambda (Paradigma Funcional)

```python
def filtroPar(a):
    return [i for i in filter(lambda b: b % 2 == 0, a)]

print(filtroPar(range(10)))
```

## Recursão + Compreensão de Lista (Paradigma Funcional)

```python
def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 2) + fibonacci(n - 1)

n = int(input("Fibonacci - Insira o tamanho da lista da sequência de Fibonacci à ser gerada: "))

print(f"Lista dos {n} primeiros valores da sequência de Fibonacci: {[fibonacci(i) for i in range(n)]}")
```

# Benchmarks

Por meio do projeto ["The Computer Language Benchmarks Game"](https://benchmarksgame-team.pages.debian.net/benchmarksgame), é possível obter diversos benchmarks da linguagem Python. Neles, é possível observar em vários dos testes que a linguagem em questão é extremamente lenta em comparação com linguagens como C ou Rust, com seus testes sendo executados em um tempo médio de mais de 100 vezes o tempo de execução da linguagem mais rápida (No caso, C).

![](https://benchmarksgame-team.pages.debian.net/benchmarksgame/download/fastest-more-elapsed.svg)

# Cálculo-Lambda

O cálculo-lambda é uma forma de representar funções de maneira breve, sendo extremamente versátil para uso como argumento em funções. É possível utilizar funções-lambda em Python, como já foi apresentado anteriormente, através da seguinte sintaxe:

```python
# lambda <parâmetro(s)>: <retorno>

# Exemplo - Função soma
sum = lambda a, b: a + b

# Chamada da função
print(sum(2, 3)) # 5
```

# Conclusão

A linguagem Python é uma das linguagens mais populares da atualidade, sem dúvida, devido à sua sintaxe simples e de fácil compreensão, e devido à escolha de seus desenvolvedores de mantê-la como uma linguagem fácilmente extensível, o que torna bibliotecas externas à linguagem (NumPy, por exemplo) quase tão populares quanto a própria linguagem em si, ambos os fatores criando um ambiente próspero ao uso em diversas áreas de pesquisa, onde pode ser necessário o auxílio computacional para a realização de cálculos complexos, tudo isso apesar de seu baixo desempenho em velocidade.

# Referências

https://en.wikipedia.org/wiki/Python_(programming_language)

https://benchmarksgame-team.pages.debian.net/benchmarksgame

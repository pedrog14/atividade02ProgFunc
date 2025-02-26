def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 2) + fibonacci(n - 1)


n = 10

print(
    f"Lista dos {n} primeiros valores da sequência de Fibonacci: {[fibonacci(i) for i in range(n)]}"
)

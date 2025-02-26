def filtroPar(a):
    return list(filter(lambda b: b % 2 == 0, a))


print(filtroPar(range(10)))

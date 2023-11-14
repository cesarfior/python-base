__version__ = "0.1.0"
__author__ = "cesar"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# iterable (percorriveis)
numeros = list(range(1, 11))

# para cada numero em numeros:
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        Resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {Resultado}"))
    print("#" * 18)

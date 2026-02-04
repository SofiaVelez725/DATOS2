def raiz_newton(n, i=10):
    # valor inicial
    x = n / 2

    # se repite la ecuacion de Newton
    for i in range(i):
        x = (x + n / x) / 2

    return x
# lo que hace es que llega a la raiz haciendo aproximaciones con una sumatoria
# toma el valor que le das y lo divide entre dos, de ahi suma el resultado con
# el numero original dividido entre el resultado, y lo divide entre dos otra vez
# y eso lo repite (10 veces en este caso) y se acerca a la raiz

numero = float(input("numero: "))

raizN = raiz_newton(numero)
raizP = numero ** 0.5

print("\nRaiz con Newton:", raizN)
print("Raiz con python:", raizP)

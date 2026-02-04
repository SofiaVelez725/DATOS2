# todo se parece un monton a los codigos en assembly porque es en binario
# si uno medio sabe assembly es facil entender
# sumar binarios
def suma_binaria(a, b):
    resultado = []

    # el carry
    carry = 0

    # se igualan en tamaño para sumar bit por bit
    while len(a) < len(b):
        a.insert(0, 0)
    while len(b) < len(a):
        b.insert(0, 0)

    # derecha a izquierda como cuando se suma
    for i in range(len(a) - 1, -1, -1):
        suma = a[i] + b[i] + carry

        # el resultdo es mod 2
        resultado.insert(0, suma % 2)

        # el carry la division entera entre 2
        carry = suma // 2

    # si al final queda carry se agrega
    if carry == 1:
        resultado.insert(0, 1)

    return resultado


# multiplicacion 
def multiplicacion_binaria(bin1, bin2):
    # eempezar en 0
    resultado = [0]

    # derecha a izquierda, los bits dicen si se suma o no
    for i in range(len(bin2) - 1, -1, -1):

        # si el bit es 1 se suma el primer numero
        if bin2[i] == 1:

            # se copia 
            parcial = bin1.copy()

            # el desplazamiento depende de la posicion del bit
            desplazamiento = len(bin2) - 1 - i
            parcial.extend([0] * desplazamiento)

            # se pone todo en el acumulado
            resultado = suma_binaria(resultado, parcial)


    return resultado



bin1 = list(map(int, input("primer binario: ")))
bin2 = list(map(int, input("segundo binario: ")))


resultado = multiplicacion_binaria(bin1, bin2)


print("resultado:")
print("".join(map(str, resultado)))

def karatsuba(x, y):
    # si algun numero es menor que 10, multiplicar directamente
    if x < 10 or y < 10:
        return x * y

    # se agarra el numero mas largo y se divide entre 2
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # separar los bumeros
    # a y b son las partes de x. ej x=1624-> a=16, b=24
    # c y d son las partes de y. ej y=9358-> c=93, d=58
    # m es la mitad de digitos de el numero mas largo
    a, b = divmod(x, 10 ** m)
    c, d = divmod(y, 10 ** m)

    # recursividad, solo 3 mulktiplicaciones
    # esto viene de las ecuaciones de arriba, se aplican reglas, distribuciones. ect. y se llega a esto
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)

    # por reglas y despeje se llega a esto
    ad_bc = ab_cd - ac - bd

    # se combinan los resultdos y ya
    return (ac * 10 ** (2 * m)) + (ad_bc * 10 ** m) + bd



x = int(input("primer numero: "))
y = int(input("segundo numero: "))

print("con Karatsuba:", karatsuba(x, y))
print("con x * y:", x * y)

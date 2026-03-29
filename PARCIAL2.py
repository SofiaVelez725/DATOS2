#producto
class Producto:
    def __init__(self, nombre, precio, utilidad):
        self.nombre = nombre
        self.precio = precio
        self.utilidad = utilidad

#algoritmo
def backtracking(productos, presupuesto, indice, 
                 costo_actual, utilidad_actual, 
                 combinacion_actual):

    global mejor_utilidad
    global mejor_combinacion

    # si el costo supera el presupuesto, detener búsqueda
    if costo_actual > presupuesto:
        return

    # ya se evaluaron todos los productos
    if indice == len(productos):
        # Verificar si es mejor solucion
        if utilidad_actual > mejor_utilidad:
            mejor_utilidad = utilidad_actual
            mejor_combinacion = combinacion_actual.copy()
        return

    #incluir el producto
    producto = productos[indice]
    combinacion_actual.append(producto)

    backtracking(
        productos,
        presupuesto,
        indice + 1,
        costo_actual + producto.precio,
        utilidad_actual + producto.utilidad,
        combinacion_actual
    )

    # backtrack
    combinacion_actual.pop()

  
    # no incluir producto
    backtracking(
        productos,
        presupuesto,
        indice + 1,
        costo_actual,
        utilidad_actual,
        combinacion_actual
    )


# main

presupuesto = int(input("Ingrese el presupuesto total: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

productos = []

for i in range(cantidad):
    print(f"\nProducto {i+1}")
    nombre = input("Nombre: ")
    precio = int(input("Precio: "))
    utilidad = int(input("Prioridad (1=bajo, 2=medio, 3=alto): "))

    productos.append(Producto(nombre, precio, utilidad))

# variables globales
mejor_utilidad = 0
mejor_combinacion = []

# hacer la busqueda
backtracking(
    productos,
    presupuesto,
    0,          # i inicial
    0,          # costo acumulado
    0,          # utilidad acumulada
    []          # combinacion temporal
)


print("\nMEJOR COMBINACIÓN ENCONTRADA")

costo_total = 0

for producto in mejor_combinacion:
    print(f"- {producto.nombre} (${producto.precio}) - Utilidad {producto.utilidad}")
    costo_total += producto.precio

print(f"Costo total: ${costo_total}")
print(f"Utilidad total: {mejor_utilidad}")

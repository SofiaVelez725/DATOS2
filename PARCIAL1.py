A = [
	[2, 3, 1],
	[4, 2, 5],
	[3, 6, 2],
	[5, 1, 4],
	[1, 4, 3],
  [6, 2, 1],
	[2, 5, 3],
  [4, 3, 6],
	[3, 1, 4],
  [5, 4, 2],
	
]

B = [
	[6, 4, 7, 6, 2, 8, 9, 5, 3, 4],
	[5, 8, 6, 3, 7, 2, 1, 9, 4, 6],
	[9, 3, 5, 2, 8, 1, 7, 4, 6, 3],
]

# Ver que la matriz sea valida
def MValida(matriz):
	if not matriz or not isinstance(matriz, list):
		return False
	columnas = len(matriz[0])
	if columnas == 0:
		return False
	for fila in matriz:
		if not isinstance(fila, list) or len(fila) != columnas:
			return False
	return True

# Ver que si se puedan multiplicar
def Multiplicables(a, b):
	if not MValida(a) or not MValida(b):
		return False
	return len(a[0]) == len(b)

# Multiplicar las matrices
def Mult(a, b):
	filas_a = len(a)
	columnas_b = len(b[0])
	columnas_a = len(a[0])

	c = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

	for i in range(filas_a):
		for k in range(columnas_b):
			acumulado = 0
			for j in range(columnas_a):
				acumulado += a[i][j] * b[j][k]
			c[i][k] = acumulado

	return c

# print a la matriz en consola
def PrintM(matriz, nombre):
	print(f"\nMatriz {nombre}:")
	for fila in matriz:
		print(fila)

# solicitud al usuario
def PreguntarFase(total_fases):
	while True:
		entrada = input(f"\nIngrese la fase a consultar (1 a {total_fases}): ")

		fase = int(entrada)
		if 1 <= fase <= total_fases:
			return fase - 1

		print("Invalido")

# Buscar el dev con mayor puntaje
def MejorDev(c, fase_k):
	mayor_actual = c[0][fase_k]
	mejor_dev = 0

	for i in range(len(c)):
		if c[i][fase_k] > mayor_actual:
			mayor_actual = c[i][fase_k]
			mejor_dev = i

	return mejor_dev, mayor_actual

# Main
def main():
	if not Multiplicables(A, B):
		print("Las matrices no se pueden multiplicar.")
		return

	C = Mult(A, B)

	PrintM(A, "A (puntos por proyecto)")
	PrintM(B, "B (horas por fase)")
	PrintM(C, "C = A x B (puntaje por desarrollador y fase)")

	fase_k = PreguntarFase(len(C[0]))
	mejor_dev, mayor_actual = MejorDev(C, fase_k)

	print(f"\nFase seleccionada: {fase_k + 1}")
	print(f"Desarrollador más productivo: Dev {mejor_dev + 1}")
	print(f"Puntaje: {mayor_actual}")


if __name__ == "__main__":
	main()

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"
modulo = num1 % num2 if num2 != 0 else "No se puede realizar módulo con cero"

# Mostrar los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")
print(f"El módulo de {num1} y {num2} es: {modulo}")


def calcular_precio_final(precio_original, descuento):
    precio_final = precio_original - (precio_original * descuento)
    return precio_final

# Ejemplo de uso
precio_original = float(input("Introduce el precio del artículo: "))
descuento = 0.15  # Descuento del 15%

precio_final = calcular_precio_final(precio_original, descuento)

print(f"El precio final después de aplicar un descuento del 15% es: {precio_final:.2f}")
num = 10

# Aumentar en 5
num += 5
print(f"Después de aumentar en 5: {num}")

# Reducir en 3
num -= 3
print(f"Después de reducir en 3: {num}")

# Multiplicar por 2
num *= 2
print(f"Después de multiplicar por 2: {num}")

# Dividir entre 4
num /= 4
print(f"Después de dividir entre 4: {num}")
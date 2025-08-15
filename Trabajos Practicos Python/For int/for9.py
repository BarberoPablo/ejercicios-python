print("Contienen dígito. Pedir dos números y un dígito. Mostrar todos los números entre ellos incluyéndolos, que poseen el dígito pedido")

num1 = int(input("Ingrese su primer numero"))
num2 = int(input("Ingrese su segundo numero"))
digito = int(input("Ingrese el digito de 0-9 a buscar"))


for numero in range(num1, num2 + 1):
  if str(digito) in str(numero):
    print(numero)


""" # Sin strings:
# Recorremos todos los números del rango
for numero in range(num1, num2 + 1):
    n = numero  # hacemos una copia para manipularla
    encontrado = False

    # Revisamos todos los dígitos del número
    while n > 0:
        if n % 10 == digito:  # sacamos el último dígito y comparamos
            encontrado = True
            break  # ya encontramos el dígito, no hace falta seguir
        n = n // 10  # eliminamos el último dígito

    if encontrado:
        print(numero) """
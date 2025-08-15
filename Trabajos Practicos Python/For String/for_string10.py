# Ejercicio 10: Iniciales de un nombre completo con puntos entre medio

nombre_completo = input("Ingrese su nombre: ")
iniciales = ""

for caracter in nombre_completo:
    if caracter == " ":
        iniciales += "."
    else:
        if "A" <= caracter <= "Z":
            iniciales += caracter
            
iniciales += "."

print("Iniciales:", iniciales)


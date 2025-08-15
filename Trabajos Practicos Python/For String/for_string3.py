# Ejercicio 3: Eliminar signos de puntuación
# Eliminar simbolos . , ; : ! ? ¿ ¡ " ( ) de la frase del usuario y devolverla limpia

frase = input("Ingrese una frase: ")

frase_limpia = ""

for caracter in frase:
  if caracter != '.' and caracter != ',' and caracter != ';' and caracter != ':' \
   and caracter != '!' and caracter != '?' and caracter != '¿' and caracter != '¡' \
   and caracter != '"' and caracter != '(' and caracter != ')':
    frase_limpia = frase_limpia + caracter

print("Frase limpia:", frase_limpia)

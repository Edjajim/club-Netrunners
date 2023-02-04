mensaje = input("Ingrese su mensaje: ")
mensaje = mensaje.replace(" ", "")
costo = 0
acentos = "áéíóúÁÉÍÓÚñÑ"

for caracter in mensaje:
    if caracter.isnumeric():
        costo += 2
    elif caracter in acentos:
        costo +=3
    elif caracter.isalpha():
        costo += 1
    else:
        costo += 3

print("El costo de su mensaje es $", costo)
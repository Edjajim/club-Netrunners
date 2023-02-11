frase = input("Ingresa la frase: ").upper()
mostrar = ""

cifrado = {"M":"0", "U":"1", "R":"2", "C":"3", "I":"4", "E":"5", "L":"6", "A":"7", "G":"8", "O":"9"}

print("1. Encriptar")
print("2. Desencriptar")
opc = int(input())

for element in frase:
    try:
        if opc == 1:
            letra = cifrado[element]
        else:
#Convierte en lista las claves del diccionario para manejarlos mediante index
#Para indicar el index a utilizar convierte en lista los valores para poder usar el método de obtener el index según el caracter correspondiente
            letra = list(cifrado.keys())[list(cifrado.values()).index(element)]
    except:
        letra = element

    mostrar = mostrar + letra

print(mostrar)
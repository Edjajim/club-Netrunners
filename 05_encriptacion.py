frase = input("Ingresa la frase: ")
frase = frase.upper()
mostrar = ""

cifrado = {"M":"0", "U":"1", "R":"2", "C":"3", "I":"4", "E":"5", "L":"6", "A":"7", "G":"8", "O":"9"}
descifrar = {"0":"M", "1":"U", "2":"R", "3":"C", "4":"I", "5":"E", "6":"L", "7":"A", "8":"G", "9":"O"}

#Encriptar
def encriptar(frase, mostrar):
    for element in frase:
        try:
            letra = cifrado[element]
        except:
            letra = element

        mostrar = mostrar + letra
    
    print(mostrar)

#Desencriptar
def desencriptar(frase, mostrar):
    for element in frase:
        try:
            letra = descifrar[element]
        except:
            letra = element

        mostrar = mostrar + letra

    print(mostrar)

print("1. Encriptar")
print("2. Desencriptar")
opc = int(input())

if opc == 1:
    encriptar(frase, mostrar)
else:
    desencriptar(frase, mostrar)
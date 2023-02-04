palabra = input("Ingresa una palabra:").strip()
palabra = palabra.replace(" ", "")
palabra = palabra.replace("á", "a")
palabra = palabra.replace("é", "e")
palabra = palabra.replace("í", "i")
palabra = palabra.replace("ó", "o")
palabra = palabra.replace("ú", "u")
palabra = palabra.lower()

inversa = ''.join(reversed(palabra))



if palabra==inversa:
    print("True")
else:
    print("False")
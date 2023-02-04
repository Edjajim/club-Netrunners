a = input("Ingresa el lado a:")
b = input("Ingresa el lado b:")
c = input("Ingresa el lado c:")

a = int(a)
b = int(b)
c = int(c)

if ( a <= ( b + c ) ) and ( b <= ( a + c ) ) and ( c <= a + b ):
    print("El triángulo es válido")
else:
    print("El triángulo es inválido")
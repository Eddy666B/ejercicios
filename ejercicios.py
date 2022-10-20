"""
#Ejercicio 1
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
"""

'''
#ejercicio 2
contra = input("ingrese su contrasena: ")
contra_lower = contra.lower()

confir = input("confirme su contrasena: ")
confir_lower = confir.lower()

if contra_lower == confir_lower:
    print("su contrasena es correcta")
else:
    print("contrasena incorrecta")
'''

"""
#ejercicio 3
a = int(input("ingrese el numerador: "))
b = int(input("ingrese el denominador: "))
if b == 0:
    print("error")
    b()

resul = a/b
print("su resultado es :",resul)
"""

"""
#ejercicio 4
a = int(input("ingrese un numero entero: "))
if a % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
"""

"""
#ejercicio 5
a = int(input("ingrese su edad: "))

if a >= 18:
    b = int(input("ingrese sus ingresos mensuales: "))
    if b >= 1500:
        print("Usted tiene que Tributar")
    else:
        print("Usted no puede tributar")

else:
    print("Usted no puede tributar")
"""

'''
#ejercicio 6
A = {"F":["a","b","c","d","e","f","g","h","i","j","k","l"],"M":["o","p","q","r","s","t","u","v","w","x","y","z"]}

while True:
    s = int(input("ingrese '1' para continuar, cualquier otro caracter para finalizar: "))
    if s == 1:
        
    
        x = str(input("ingrese su sexo, 'F' si es femenino y 'M' si es masculino: "))
        if x in A.keys():
            y = str(input("ingrese su nombre: "))
            y_lower = y.lower()
            
            if y_lower[0] in A[x]:
                print("Usted pertenece al grupo A")
                
            else:
                print("Usted pertenece al grupo B")
               
        else:  
            print("Sexo mal indicado")
        
    else:
        break
'''

'''
#ejercicio 7
a = int(input("introduzca un numero entero positivo: "))
b = []
if a >= 0:

    for i in range(1,a+1):
        
        if i % 2 != 0:
            b.append(i)
else:
    print("caracter erroneo")

print("Los numeros impares hasta su numero es: ",b)
'''

'''
#ejerccio 8
a = int(input("ingrese la cantidad a invertir: "))
b = int(input("ingrese el interes anual: "))
c = int(input("ingrese el numero de años: "))

for i in range(1,c+1):
    t = a*(1+b)**i
    print("su capital en ",i," años es: ",t)

'''


#ejercicio 9

print(" clave de las bolas:\nBlanco : B\nVerde : V\nMorado : M\nCeleste : C\nRojo : R ")
producto = []
descuento = {"B":0,"V":20,"M":35,"C":60,"R":100}
a = str(input("ingrese el color de la bola: "))

b = int(input("ingrese la cantidad de productos: "))
for i in range(1,b+1):

    c = int(input(f"ingrese el precio del producto {i}: "))
    producto.append(c)

precio_total = sum(producto)-float(sum(producto)*(descuento[a]/100))

print("Precio total a pagar es: ",precio_total)

"""
#ejercicio 10
lista = []

while True:

    print("para terminar el proceso escriba el numero: 0")
    a = float(input("ingrese los galones usados: "))
    if a == 0:
        break
    b = float(input("ingrese los km conduciodos: "))
    if b == 0:
        break
    c = b/a
    print("kms/galon de este tanque fueron: ",c)
    
    lista.append(c)
    
    promedio = sum(lista)/len(lista)
    print("el promedio de general de kms/galon es: ",promedio)
    print()
"""

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

#ejercicio 10
lista = []

while True:
    a = float(input("ingrese los galones usados: "))
    b = float(input("ingrese los km conduciodos: "))
    c = b/a
    print("kms/galon de este tanque fueron: ",c)
    
    lista.append(c)
    
    promedio = sum(lista)/len(lista)
    print("el promedio de general de kms/galon es: ",promedio)


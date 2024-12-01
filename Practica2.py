#practica2
#1
edad = int(input("Digite su edad: "))
if(edad >= 18):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
#2
num=int(input("Digite un número: "))
if(num >= 0):
    print("El número es positivo")
else:
    print("El número es negativo")
#3
num=int(input("Digite un número: "))
if num%2 == 0: # % da el modulo y el modulo representa al residuo, es decir, al dividirlo entre 2 el residuo es 0
    print("El número es par")
elif num%2 == 1:
    print("El número es impar")
else:
    print("Error")
#4
contra="1234CR"
password=input("Digite su contraseña: ")
if contra == password:
    print("Acceso concedido")
else:
    print("Acceso denegado")

#5
dia=input("Digite un numero del 1 al 7: ")
match dia:
    case "1":
        print("Este número corresponde al LUNES")
    case "2":
        print("Este número corresponde al MARTES")
    case "3":
        print("Este número corresponde al MIÉRCOLES")
    case "4":
        print("Este número corresponde al JUEVES")
    case "5":
        print("Este número corresponde al VIERNES")
    case "6":
        print("Este número corresponde al SABADO")
    case "7":
        print("Este número corresponde al DOMINGO")
    case _:
        print("Este valor no corresponde a ningun día")

#6
año=int(input("Digite un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Este es un año bisiesto")
else:
    print("Este no es un año bisiesto")

#7
nota=int(input("Ingrese la calificación del estudiante:"))
match nota:
    case nota if nota >= 90 and nota <=100:
        print("La callificación es A")
    case nota if nota >= 80 and nota <=89:
        print("La calificación es B")
    case nota if nota >= 70 and nota <=79:
        print("La calificación es C")
    case nota if nota >= 60 and nota <=69:
        print("La calificación es D")
    case nota if nota >= 0 and nota < 60:
        print("La calificacición es F")
    case _:
        print("Error")

#8
ladoA=int(input("Digite la medida deL lado  1 del triangulo:"))
ladoB=int(input("Digite la medida deL lado 2 del triangulo:"))
ladoC=int(input("Digite la medida deL lado 3 del triangulo:"))

if(ladoA == ladoB == ladoC):
    print("Este es un triangulo Equilátero") #todos los lados son iguales
elif(ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC): 
    print("Este es un triangulo Isósceles") #dos lados son iguales
else:
    print("Este es un triangulo Escaleno") #todos los lados son diferentes

#9
comparacion1=int(input("Digite un numero:"))
comparacion2=int(input("Digite un numero:"))
comparacion3=int(input("Digite un numero:"))
mayor= comparacion1
if mayor < comparacion2:
    mayor = comparacion2
if mayor < comparacion3:
    mayor = comparacion3
print("El numero mayor es", mayor)

#10 
año=int(input("Digite un año: "))
if ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and  (año % 100 == 0): #% determina si es multiplo de x número
    print("Este es un año bisiesto y un siglo")
else:
    print("Este no es un año bisiesto y un siglo")
#11 
pais = ""
paises_continentes=""
while pais != "SALIR":
   pais=input("Digite el nombre del país (digite SALIR para terminar: )").upper()
   if pais in paises_continentes:
      lista = paises_continentes.split(",")
      indice=lista.index(pais)
      print(lista[indice+1])
   else:
      if pais != "SALIR":
         print("No conozco ese país, puedes decirme tu que a que continente pertenece")
         continente=input("Digite el continente: ").upper()
         paises_continentes += ","+pais+","+continente

#12
tri1=int(input("Digite la medida del lado 1:"))
tri2=int(input("Digite la medida del lado 2:"))
tri3=int(input("Digite la medida del lado 3:"))
if tri1**2 + tri2**2 == tri3**2:
        print ("Triangulo rectángulo")
elif tri1**2 + tri2**2 < tri3**2:
        print ("Triangulo obtusángulo")
else:
        print ("triangulo acutángulo")

#13
edadC1=int(input("Digite la edad 1:"))
edadC2=int(input("Digite la edad 2:"))
edadC3=int(input("Digite la edad 3:"))
restEdad= (edadC1 + edadC2 + edadC3) / 3
print("El promedio de las edades es:", restEdad)

#14 
numeroPrimo= int(input("Digite un numero:"))
if numeroPrimo <= 1:
    print("Este no es un numero primo")
if(numeroPrimo == 2 or numeroPrimo == 3):
     print("Este es un numero primo")
elif (numeroPrimo % 2 == 0 or numeroPrimo % 3 == 0):
     print("Este no es un numero primo")

#15
numeroMultiplo= int(input("Digite un numero:"))
if numeroMultiplo % 5 == 0 or numeroMultiplo % 7 == 0:
     print("Este es un numero multiplo del 5 o 7")
else:
     print("Este no es un numero multiplo del 5 o 7")


## Basic Learning 

## Inicializacion de python. Hola Mundo

print("Hola Mundo. Esto es un tutorial basico de python")

## Las Variables se guardan de la siguiente manera 

print("Los numeros no se pueden concatenar directamente a texto.")

##Esto abajo da un error
##print(12+"2") 

print("Pero se pueden separar por comas en print al menos ", 12)

## las variables se pueden nombrar de manera dinamica (buscar termino correcto)

foo = "Bar"

print (foo)

print("Separado por coma", "El texto se ve asi ", foo)

foo = 12

print (foo)

print("Separado por coma", "Tambien se puede poner numeros", foo)
## Podemos tener un input directo desde consola, considerandolo como string

inputVar = input("Ingrese un string")

print("Emitio : ", inputVar)

print(type(inputVar))

## y hay varios tipos de variables 

intVar = 12 
boolVar = False
stringVar = "Hello"
floatVar = 1.2

print(type(intVar))
print(type(boolVar))
print(type(stringVar))
print(type(floatVar))

if isinstance(intVar,int) : print( "Intvar es un numero")
else : print("Eso no es un numero")


## Strings 

## se pueden parsear los strings directos 
some = "Body once told me"
the = "World was gonna roll me"
print ( some+the)

## los strigs de comillas sencillas pueden ayudar a imprimir los de comillas dobles

someDoblecomillas = ' Quiero poner "comillas dobles " '
print(someDoblecomillas)

## y viceversa

somedobleCencillas = "Y a veces usar las se'n cillas "
print (somedobleCencillas)

## tambien podemos hacer cadenas locas 

print("NANANANANA"*12+"BATMAN")

## Formaateando

AC = 12
HP = 20

template = "Monster with AC {} and HP {}".format(AC,HP)

print(template)

templateAunMasSencilla= f"Monster with AC{AC} and HP {HP}"

print(templateAunMasSencilla)

# Numeros 

## Podemos cambiar los numeros enteros con calma. 
## Recuerdan la ac??

#Demosle un escudo a nuestro monsutro 

input("Demosle un escudo al Monstruo")

AC = AC + 2

templateAunMasSencilla= f"Monster with AC {AC} and HP {HP}"

print(templateAunMasSencilla)

input("Demosle otro escudo al Monstruo")
AC += 2
templateAunMasSencilla= f"Monster with AC {AC} and HP {HP}"

print(templateAunMasSencilla)

## NUmeros muy altos se convierten en notacion cientifica! 

cient=0.*0.0000123

print(cient)
## EMOSIDO ENGAÑADO
## O depende del ambiente de python. pereza re rechequear

##Si se pueden ejecutar todo tipo de operaciones e imprimirlas 

print (2+2)
print (2*2)
print (2-2)
print (2/2)
print(49%2) # Modulo
print (7//3) #Solo el entero
print (2 ** 3) ## Elevado a

## Parseando: Se usa directo la funcion

AC = int(input("Enter the AC of the Mosnter"))
templateAunMasSencilla= f"Monster with AC {AC} and HP {HP}"

print(templateAunMasSencilla)

someNumber= 12

print("Printing a Number! "+str(someNumber))

## Comparadores y logica 

#This is true
print (10 > 3)

#this is false 
print(10 < 3)

## Los mayor igual, o menor igual son con el comparador a la iquierda

print (3>=3)

print (4<=4)

## Igual y falso son los clasicos 

print("A"=="A")

print("A"=="B")

print("A"=="a")







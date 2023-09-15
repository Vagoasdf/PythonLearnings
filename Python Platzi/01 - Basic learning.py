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

## podemos buscar cosas en textos!

pajar="PAAAAAAAagujaAAAAAJAAAR"
print("Buscando Aguja en un pajar", pajar)
print("aguja" in pajar)
print("Era un gran pajar, observa: ", len(pajar))
## Pero los busca en mayusculs? 

pajarMayus = pajar.upper()
print("Buscando Aguja en un pajar", pajarMayus)
print("aguja" in pajarMayus)

## Existen tambien startsWith, endsWith, como booleanos para comprobar
# replace, para cambiar un texto 
# replace y capitalize, 

## Print y formatos

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


# Puntos Flotantes y particularidades 

a = 1.12 

b = 2.34

# Puntos Flotantes

c = a+b 

d = 3.46

print (a)
print (b)
print (c)
print(d)
## Osea qeue hacer la comparacion es mas completa, se va a la b
print(c==d)

## Podemos intentar ahi si cambiar el formato 
floatAsStr=format(c,".3g")
print(floatAsStr)

## Podemos tambien añadir una tolerancia,e s decir, cuandas comillas le aceptamos

tolerance = 0.001
print(abs(c-d) < tolerance)
## Entonces, si la diferencia es menor a 0.001, lo consideramos igual


# Operadores Logicos

##AND
print("AND") 
print (True and True)
print (True and False)
print (False and False)
print(10*"***")
##OR
print ("OR")
print (True or True)
print (True or False)
print (False or False)
print(10*"***")

## not
print ("not")
print (not True)
print (not False)

# Estructuras de datos basicas 

## Indices y Slicing con strings
 
text="un ejemplo para ver Indexing"
print(text)
print(text[:12])
print(text[2:12])
#pero no nos da el final??
print(text[-12:-1])
##entonces al final
print(text[5:])
print(text[-12:])
## Y tambien nos podemos ir saltando!
print(text[2:22:3])
## vamos del inicio al fin saltando 
print(text[::2])
print(text[1::2])

## Listas, CRUD BASICO 

#Create 
lista = [10,29,33,44,55]
lista.insert(2,123)

#Read
print(lista[2])
print(lista)

# Update 
lista[1]=22
print(lista)

otherList = [12,33,55,66,1231,213]

combinedList = lista+otherList
print(combinedList)

combinedList.reverse()
print(combinedList)


##buscar indices 

index = combinedList.index(33)
print(index)


#Delete.
combinedList.remove(33)
index = combinedList.index(33)
print(index)

combinedList.pop()
print(combinedList)

combinedList.pop(0)
print(combinedList)

combinedList.pop(5)
print(combinedList)

combinedList.sort()
print(combinedList)

## Tuplas
tuplaNumerica = (1,2,3,4)
print(tuplaNumerica)
print(type(tuplaNumerica))
tuplaString = ("Uno", "Dos", "Tres")
print(tuplaString)
print(type(tuplaString))
##Funciona relativamente igual con los splices
print(tuplaNumerica[2])

##Ahora la tupla lo que tiene especial es que solo se declara. no se puede 
##añadir nada mas
#tuplaNumerica.append ##no existe
##Es una estructura de datos de solo lectura

tuplaRepetida = ( 11,22,11,44,31,21)
print(tuplaRepetida.count(11))
listaRepetida = [11,22,11,44,31,21]
print(listaRepetida.count(11))
## Sigo sin ver las ventajas de la Tupla. 
## a si que mejor la convertimos en lista lol 
listadeTupla = list(tuplaRepetida)
## tambien al verre
tuplaDeLista = tuple(listaRepetida)

## Diccionarios




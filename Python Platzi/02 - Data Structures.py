
#Sets

country_sets = {"chile", "ecuador", "argentina"}

multi_sets = {12, "hello"}

print(multi_sets)

## Podemos hacer sets a traves de Listas, etc etc 

## y tambien adiciones basicas
country_sets.add("laconia")

country_sets.remove("chile")

country_sets.discard("laputa")

print(country_sets)

## pero tambien podemos hacer las aritmeticas de conjuntos

setA = {"some", "strings", "here"}
setB = {"some", "integers", 12,24}

setUnited = setA | setB
print (setUnited)

setIntersected = setA & setB
print (setIntersected)

setRemoved = setA - setB
print(setRemoved)

setRemoved = setB - setA
print(setRemoved)

###Algo cool. Diferencia simetrica (Outer Union)
setSimetric = setA^setB
print(setSimetric  )

#List Comprehensions

print ("#### LIST COMPREHENSIONS ####")
numbers = []
for element in range(1,15):
    numbers.append(element)

print(numbers)

numbersV2 = [element for element in range(1,12)]
print(numbersV2)

## y se juega
numbersEscalating = [element**2 for element in range(1,12)]
print(numbersEscalating)

## y se va a la tsutsa
numbersOnlyPairs = [element**2 for element in range(1,12) if (element%2==0)]
print(numbersOnlyPairs)


# DICT COMPREHENSIONS!
dictOnlyPairPowers = {element : element**2 for element in range(1,12) if (element%2==0)}
print(dictOnlyPairPowers)

## Usable para recorrer listas oye
countriesLists = [ "col", "ecu", "chi", "arg"]
import random 

pctRandomnes = {country : random.randint(0,100) for country in countriesLists}
print(pctRandomnes)

## Para juntar dos listas de mismo tamaño 
weaponNames = ["Weapon1", "weapon2", "weapon3"]
diceDamage = ["2d4","3d6","1d6"]
zippedList = zip(weaponNames,diceDamage)
print(zippedList)
weaponAndDamage = { name : damage for (name, damage) in zip(weaponNames,diceDamage) }
print(weaponAndDamage)

grabVowels = "text with vowels"

vowels = { vow:vow for vow in grabVowels if vow in "aeiou"}
print (vowels)


## Final entre Lists vs Tuplas vs Sets

## Listas: Mutables, Ordenadas, se puede hacer index y slice
## Tuplas: Listas no mutables 
## Set: sets mutables, pero no ordenada, ni indicie, ni se pueden duplicar elementos

# Funciones y Lambdas 
def reverse(s):
    return s[::-1]

reverseLambda = lambda s: s[::-1]

print (reverse("A STRING! "))

print(reverseLambda("A LAMBDA STRING!"))

## Funciones con multiples returns 

def find2DPropeties(width, length):
    return width*length, width*2+length*2

area, perimetro = find2DPropeties(10,20)

print(area,perimetro )

TwoDLambda = lambda a,b : (a*b, a*2+b*2)

area, perimetro = TwoDLambda(4,6)

print(area,perimetro )

## High Order Functions

##Podemos pasarle funciones a funciones para ejecutarles adentro

def scaleUpper(x):
    return x+x+1

def executeFunction(function,times):
    acum = 0 
    for i in range(1,times):
        acum =function(acum)
    return acum

result = executeFunction(scaleUpper,4)
print(result)
## Lambda tiene ciertas limitaciones. No se pueden ejecutar las cosas grandes
lambdaUpper = lambda x : x*2+1

lambdaExecute = lambda times, function : times*function(times)

print(lambdaExecute)

## Map. Un ejemplo de High Order Function

numbers = [number for number in range(1,12)]

print (numbers)

numbersV3  = map(lambda i: i*2, numbers)
print(list(numbersV3))

##sumarListas. Ojo que solo toma la lista mas pequeña. 

listaUno= [4,4,3]
listaDos = [3,5,1,1]
result = map(lambda x,y : x+y, listaUno, listaDos)

print(list(result))

## Usualmente se usan dicts, so:

weapons=[
    {
        "name" : "lazerSword",
        "range": 2,
        "damage": 8,
        "desc" : " A Powerful Sword. Can cut size 1 Mechas in half on a crit. Meele range"
    },
    {
        "name" : "cannonLazer",
        "range": 4,
        "damage": 6,
        "desc" : "One beam into destruction. Can wreck havock in a line. Medium range" 
    },
    {
        "name" : "baseMachinegun",
        "range" : 6,
        "damage": 4,
        "desc" : "A machine gun strapped into an arm. Reliable an fast. Medium Range" 
    },
    {
        "name" : "ArtilleryAhoy",
        "range" : 10,
        "damage": 8,
        "desc" : "The old kinetick artillery never grows old. Long range. Slow" 
    }
]

damages = list(map(lambda weapon: weapon["damage"],weapons))

print(damages)

## nota: los Maps deben ser Inmutables. Idealmente osea


# Filters: Seleccionar elementos en listas

numbers = [number for number in range(1,12)]

pares = list(filter(lambda x : x % 2 ==0,numbers))

print (numbers)

print(pares)

## Filer con Dict
print (weapons)

## Filtrar armas de solo midRange (3 a 8 rango)

midRange = list(filter(lambda weapon : 8 > weapon["range"] > 3, weapons))

print(midRange)

# Reduce
## Reducir a un solo valor

import functools

result = functools.reduce(lambda counter, item: counter +item, numbers)

print (result)

## Modulos Cools

import sys
print (sys.path)
print(sys.hash_info)

import time 

timestamp = time.time()
local = time.localtime()
asctime = time.asctime(local)

print(timestamp, local, asctime)

import collections 

numbers = [1,2,1,1,2,2,3,4,3,3,3,2,1,3,3,4,3,2]

counter = collections.Counter(numbers)
print(counter)

### los Modulos propios, son archivos creados dentro de un py. Ver lo de modules

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


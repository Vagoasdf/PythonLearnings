## Some mods for 02
import random

def getWeapons():
    weapons=(
        {
              "name" : "lazerSword",
                "desc" : " A Powerful Sword. Can cut size 1 Mechas in half on a crit. Meele range"
        },
        {
            "name" : "cannonLazer",
            "desc" : "One beam into destruction. Can wreck havock in a line. Medium range" 
        },
        {
            "name" : "baseMachinegun",
            "desc" : "A machine gun strapped into an arm. Reliable an fast. Medium Range" 
        },
        {
            "name" : "ArtilleryAhoy",
            "desc" : "The old kinetick artillery never grows old. Long range. Slow" 
        },
    )

    return weapons

def dealDamage(maxDamage):
    return random.randint(1,maxDamage)
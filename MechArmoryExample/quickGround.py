## Ejemplo mas Avanzado 
# Honestamente Platzi esta ahi lentito, voy a tomarlo como un repoaso para las cosasa raras
# pero tengo 0 intencion de repetir un FuzzBazz basico en python

## MECH ARMORY 

# GLADIUS-Class Shield 

print(10*"*-*")
print("Mecha Armory -- Deploy Status.")

## mecha base status: 
Armor = 2
chassis = 10
movement = 5
selectedWeapon = ""
freeHand = ""
shieldDeployed = False

print ("CURRENT ARMOR: ", Armor)
print ("Shield Deployed", shieldDeployed)

if not shieldDeployed:
    equipShield = input("Want to equip shield? y/n")
    if(equipShield.lower()=="y"):
        shieldDeployed = True
        Armor +=2
        freeHand = "Shield"


if shieldDeployed:
    unequipShield = input("Want to unequip shield? y/n")
    if(unequipShield.lower()=="y"):
        shieldDeployed = False
        Armor -=2
        freehand = ""


print ("CURRENT ARMOR: ", Armor)

seeArmory=input("Want to check your armory? y/n")
if(seeArmory.lower()=="y"):
    ## Check Armory
    ## Mejoras pposibles: funcion. Matriz multinivel, base de datos. indicador
    print("Present weapons:)")
    weapons=("lazerSword","cannonLazer","baseMachinegun","ArtilleryAhoy")

    for weapon in weapons :
        print(weapon)
        if(weapon == "lazerSword"):
            print(" A Powerful Sword. Can cut size 1 Mechas in half on a crit. Meele range")
        if(weapon == "cannonLazer"):
            print("One beam into destruction. Can wreck havock in a line. Medium range")
        if(weapon == "baseMachinegun"):
            print("A machine gun strapped into an arm. Reliable an fast. Medium Range")
        if(weapon == "ArtilleryAhoy"):
            print("The old kinetick artillery never grows old. Long range. Slow")
        selectWeapon=input("Want to select the weapon ? y/n")
        if(selectWeapon.lower()=="y"):
            selectedWeapon = weapon
            break;
    
    print("Selected Weapon: ", selectedWeapon)
else:
    print("Ok shield guy, good luck.")



ready = input("Ready for Deploy? y/n")
if(ready.lower()=="y"):
    print("Good Speed")
    exit
## Ejemplo mas Avanzado 
# Honestamente Platzi esta ahi lentito, voy a tomarlo como un repoaso para las cosasa raras
# pero tengo 0 intencion de repetir un FuzzBazz basico en python

## MECH ARMORY 
print(10*"*-*")
print("Mecha Armory -- Deploy Status.")

## mecha base status: 
mechStatus= {
    "Armor" : 2,
    "chassis" : 10,
    "movement" : 5,
    "selectedWeapon" : "",
    "freeHand" : "",
    "shieldDeployed" : False,
}

settingArmory = True

while settingArmory:
    print ("CURRENT ARMOR: ", mechStatus["Armor"])

    if not mechStatus["shieldDeployed"]:
        equipShield = input("Want to equip shield? y/n")
        if(equipShield.lower()=="y"):
            mechStatus["shieldDeployed"] = True
            mechStatus["Armor"] +=2
            mechStatus["freeHand"] = "Shield"

    elif mechStatus["shieldDeployed"]:
        unequipShield = input("Want to unequip shield? y/n")
        if(unequipShield.lower()=="y"):
            mechStatus["shieldDeployed"] = False
            mechStatus["Armor"] -=2
            mechStatus["freeHand"] = "None"

    print("Weapon deployed: ",mechStatus["selectedWeapon"])
    print("Free hand:", mechStatus["freeHand"])
    seeArmory=input("Want to check your armory? y/n")
    if(seeArmory.lower()=="y"):
        ## Check Armory
        ## Mejoras pposibles: funcion.  base de datos. indicador
        print("Selecting main Weapon:")
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

        for weapon in weapons :
            print(weapon["name"])
            print(weapon["desc"])
            selectWeapon=input("Want to select the weapon ? y/n")
            if(selectWeapon.lower()=="y"):
                mechStatus["selectedWeapon"] = weapon
                break;
        
        print("Selected Weapon: ", mechStatus["selectedWeapon"])

        if (mechStatus["freeHand"] != "Shield") :
            print("Select Weapon for Freehand. Current: ", mechStatus["freeHand"])
            for weapon in weapons :
                print(weapon["name"])
                print(weapon["desc"])
                selectWeapon=input("Want to select the weapon ? y/n")
                if(selectWeapon.lower()=="y"):
                    mechStatus["freeHand"] = weapon
                    break;
        
        print("OffHand Weapon: ", mechStatus["freeHand"])
        
    ready = input("Ready for Deploy? y/n")
    if(ready.lower()=="y"):
        print("Good Speed")
        settingArmory = False

print("----- ARMORY SET UP. GOOD SPEED CAVALIER -------")
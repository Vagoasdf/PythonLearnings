def confirm(confirmText):
    confirm=input(confirmText)
    return confirm.lower()=="y"


class Mecha:
    def __init__(self, armour, chassis,speed):
        self.armour = armour
        self.chassis = chassis
        self.chassis = speed
        self.shieldDeployed = False
        self.selectedWeapon = None
        self.freeHand = None
    


    def deployShield(self):
        if not self.shieldDeployed and confirm("Want to equip shield? y/n"):
                self.shieldDeployed = True
                self.armour +=2
                self.freeHand = "Shield"

        elif(confirm("Want to equip shield? y/n")):
                self.shieldDeployed = False
                self.armour -=2
                self.freeHand = None

    def checkArmoury(self):  
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
            print(weapon["name"], weapon["desc"])
            if(confirm("Want to select the weapon ? y/n")):
                self.selectedWeapon = weapon
                break;
        print("Selected Weapon: ", self.selectedWeapon)

        if (self.freeHand != "Shield") :
            print("Select Weapon for Freehand. Current: ", self.freeHand)
            for weapon in weapons :
                print(weapon["name"], weapon["desc"])
                if(confirm("Want to select the weapon ? y/n")):
                    self.freeHand = weapon
                    break;
        print("OffHand Weapon: ",  self.freeHand)



settingArmory = True
mecha = Mecha(5,10,5)

while settingArmory:
## MECH ARMORY 
    print(10*"*-*")
    print("Mecha Armory -- Deploy Status.")

    print(mecha.chassis, mecha.armour,mecha.selectedWeapon)

    mecha.deployShield()

    if confirm("Want to check Armory? y/n"):
        mecha.checkArmoury()

    if confirm("Ready for Deploy? y/n"):
        settingArmory = False

print("----- ARMORY SET UP. GOOD SPEED CAVALIER -------")
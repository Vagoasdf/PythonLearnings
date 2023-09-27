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
    
   


    def deployShield(selielf):
        if not self.shdDeployed and confirm("Want to equip shield? y/n"):
                self.shieldDeployed = True
                self.armour +=2
                self.freeHand = "Shield"

        elif(confirm("Want to equip shield? y/n")):
                self.shieldDeployed = False
                self.armour -=2
                self.freeHand = None

    def checkArmoury(self):  
        print("Selecting main Weapon:")


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
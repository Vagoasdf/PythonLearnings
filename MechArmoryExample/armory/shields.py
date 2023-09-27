
def confirm(confirmText):
    confirm=input(confirmText)
    return confirm.lower()=="y"


def deployShield(self):
    if not self.shieldDeployed and confirm("Want to equip shield? y/n"):
            self.shieldDeployed = True
            self.armour +=2
            self.freeHand = "Shield"

    elif(confirm("Want to equip shield? y/n")):
            self.shieldDeployed = False
            self.armour -=2
            self.freeHand = None

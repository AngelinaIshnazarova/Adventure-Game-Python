import time
import random


def print_pause(*args):
    global monster, weapon

    print(*args)
    time.sleep(2)


def input_validation(message):
    while True:
        choice = input(message).strip()

        if choice in ("1", "2"):
            return int(choice)


def house():

    global weapon

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps",
                f"a {monster}.")
    print_pause(f"Eep! This is a {monster}'s house!")
    print_pause(f"The {monster} attacks you!")

    if has_sword is False:
        print_pause("You feel a bit under-prepared for this, what with only",
                    "having a tiny dagger.")

    choice = input_validation("Would you like to (1) fight or (2) run away? ")

    if choice == 1:
        return fight()

    elif choice == 2:

        print_pause("You run back into the field. Luckily, you don't seem",
                    "to have been followed.")
        return field()


def fight():

    global monster, weapon, has_sword

    if has_sword is False:

        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {monster}.")

        return False

    else:
        print_pause(f"As the {monster} moves to attack, you unsheathe your",
                    "new weapon.")
        print_pause("The " + weapon + " shines brightly in your hand as you brace",
                    "yourself for the attack.")
        print_pause(f"But the {monster} take one look at your shiny new toy",
                    "runs away!")

        return True


def field():

    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choice = input_validation("(Please enter 1 or 2.)\n")

    if choice == 1:
        return house()

    elif choice == 2:
        return cave()


def cave():

    global has_sword, monster

    print_pause("You peer cautiously into the cave.")

    if has_sword is False:

        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon + " !")
        print_pause("You discard your silly old dagger and take the sword",
                    "with you.")
        has_sword = True

    else:

        print_pause("You've been here before, and gotten all the good stuff",
                    "It's just an empty cave now.")

    print_pause("You walk back out to the field.")
    return field()



def main():

    global has_sword, monster, weapon
    has_sword = False

    monster = random.choice(["wicked fairie", "gorgon", "troll"])
    weapon = ("Sword of Ogoroth")

    print_pause("You find yourself standing in an open field, filled with",
                "grass and yellow woldflowers.")
    print_pause("Rumour has it that a wicked fairie is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)",
                "dagger.")

    win = field()

    if win:
        print_pause(f"You have rid the town of the {monster}.",
                    "You are victorious!")

    else:
        print_pause("You have been defeated!")


if __name__ == "__main__":

    while True:

        main()

        ans = input("Would you like to play again (y/n) ?")

        if ans == "n":
            print_pause("Thanks for playing! See you next time.")
            break

        else ans == "y":
            print_pause("Excellent! Restarting the game...")
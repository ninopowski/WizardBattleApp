import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print("-----------------------")
    print("--- Wizard Game app ---")
    print("-----------------------")


def game_loop():

    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, scaliness=20, breaths_fire=True),
        Wizard("Evil Wizard", 100)
    ]

    hero = Wizard("Gandolf", 75)

    while True:

        if creatures:
            active_creature = random.choice(creatures)
        else:
            print("You've defeated all creatures")
            break

        print(f"There is a {active_creature} in front.")

        cmd = input("You [a]ttack, [r]unaway or [l]ook around? ")
        if cmd == "a":
            if hero.attack(creature=active_creature):  # if the attack is successful
                creatures.remove(active_creature)
                print(f"You have defeated the {active_creature.name}")
            else:
                print("The wizard took a beating and is hidding to recover...")
                time.sleep(5)
                print("The wizard return as new.")


        elif cmd == "r":
            print("runaway")
        elif cmd == "l":
            print(f"The wizard {hero.name} looks around and sees:")
            for c in creatures:
                print(c)
        else:
            print("Exiting the game. Bye!")
            break

        print()






if __name__ == '__main__':
    main()
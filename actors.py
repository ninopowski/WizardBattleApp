import random


class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level



class Wizard(Creature):

    def __init__(self, name, level):   # if its the same with the parent init, you dont need this init at all!!
        super().__init__(name, level)

    def attack(self, creature):
        print(f" The Wizard {self.name} attacs {creature.name}")

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f"You rolled {my_roll}.")
        print(f"The {creature.name} rolled {creature_roll}")

        if my_roll >= creature_roll:
            return True
        else:
            return False



class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        return super().get_defensive_roll() / 2   #using the parent method directly




class Dragon(Creature):

    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_modifier = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifieer = self.scaliness / 10
        return base_modifier * fire_modifier * scale_modifieer


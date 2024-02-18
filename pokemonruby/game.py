from pokemon import Pokemon
from pokedex.pokemons import Pokedex as POKEMONS
from battle import Battle
from validations import Validations

import random

class Game:

    def __init__(self):
        self.name_trainer = ""
        self.initial_poke = ""
        self.initial_poke_name = ""
        self.poke = ""
        self.current_stats = {}
        self.difficulty = 1

    def start(self):
        Validations.print_welcome(self)

        action = Validations.menu()
        while action != "Exit":
            if action == "Train":
                Game.train(self)
                action = Validations.menu()
            if action == "Leader":
                action = "Exit" if Game.challenge_leader(self) == True else Validations.menu()
            if action == "Stats":
                Game.show_stats(self)
                action = Validations.menu()
        Game.goodbye()

    def train(self):
        pokemons = POKEMONS.POKEMONS
        target = random.choice(list(pokemons.keys()))
        level = random.randint(1,int(self.poke.level) + int(self.difficulty))
        print(f"{self.name_trainer.upper()} challenge Random Person for training")
        print(f"Random Person has a {target.upper()} level {level}")
        print("What do you want to do now? \n")
        print("1. Fight        2. Leave")
        action = ""
        while action == "" or action not in ["Leave", "Fight"]:
            action = input("> ").capitalize()
            if action == "Leave":
                continue
            elif action == "Fight":
                Game.fight(self, target, level)
            else:
                print("Enter a right option:")
            

    def fight(self, target, level, o_trainer = "Random Person"):
        print(f"{o_trainer} sent out {target.upper()}!")
        print(f"{self.name_trainer} sent out {self.initial_poke_name.upper()}!")
        print("-------------------Battle Start!-------------------")
        print(f"{self.name_trainer}'s {self.initial_poke_name} - Level {self.poke.level}")
        print("HP:", self.poke.current_stats["hp"])
        print(f"{o_trainer}'s {target} - Level {level}")
        opponent = Pokemon(target)
        opponent.name = target
        opponent.level = level
        opponent.increase_stats()
        print("HP: ", opponent.current_stats["hp"])
        battle = Battle(self.name_trainer, self.poke, o_trainer, opponent)
        battle.start()
        battle.win

    def challenge_leader(self):
        win = False
        target = "Onix"
        level = 10
        print(f"{self.name_trainer.upper()} challenge the Gym Leader Brock for a fight!")
        print(f"Brock has a {target.upper()} level {level}")
        print("What do you want to do now? \n")
        print("1. Fight        2. Leave")
        while True:
            action = input("> ").capitalize()
            if action in ["Leave", "Fight"]:
                if action == "Fight":
                    win = Game.fight(self,target, level, "Brock")
            break
        
        return win

    def show_stats(self):
        print(f"\n{self.poke.name.upper()}")
        print(f"Kind: {self.poke.poke_info['species']}")
        print(f"Level: {self.poke.level}")
        print(f"Type: {(', ').join(self.poke.poke_info['type'])}")
        print("Stats:")
        labels = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]
        for i in range(0, len(labels)):
            print(f"    {labels[i].capitalize()}:", self.poke.current_stats[labels[i]])
        print("Experience Points: ", self.poke.total_experience)
        print("Experience Points to next level: ", self.poke.exp_to_next_lvl)

    def goodbye():
        print("Thanks for playing Pokemon")
        print("This game was created with love by Rodrigo, Erik, Joshua and Steph")

game = Game()
game.start()

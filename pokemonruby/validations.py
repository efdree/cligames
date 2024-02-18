from pokemon import Pokemon
from pokedex.pokemon_art import Art

class Validations:

    def menu():
        print("-----------------------Menu-----------------------\n")
        menuOptions = ["Stats", "Train", "Leader", "Exit"]
        for index, option in enumerate(menuOptions):
            print(f"{index + 1}.", option, end= "    ")
        print("")            
        action = ""
        while action not in menuOptions:
            action = input("> ").capitalize()
            if action not in menuOptions:
                print("Enter a right option:")
        return action
    
    def choose_difficulty(self):
        print("Select difficulty:\n")
        levelOfDifficulty = ["easy", "medium", "hard"]
        for index, difficulty in enumerate(levelOfDifficulty):
            print(f"{index + 1}.", difficulty.capitalize(), end= "    ")
        print("\nChoose a number:" )
        Validations.valid_difficulty(self)
        
    def is_valid_integer(input_str):
        try:
            int(input_str)
            return True  
        except ValueError:
            return False  

    def valid_difficulty(self):
        difficulty = ""
        while difficulty == "" or difficulty not in ["1", "2", "3"] :
            difficulty = input("> ")    
            if Validations.is_valid_integer(difficulty) == False:
                print("Enter a right number 1, 2 or 3:")        
            elif int(difficulty) not in [1, 2, 3]:
                print("Enter a right number between 1-3:")
        self.difficulty = difficulty
        
        
    def valid_trainer_name(self):
        name_trainer = ""
        while name_trainer == "":
            self.name_trainer = input("> ")
            if self.name_trainer != "":
                print(f"""
Right! So your name is {self.name_trainer.upper()}!
Your very own POKEMON legend is about to unfold! A world of
dreams and adventures with POKEMON awaits! Let's go!
Here, {self.name_trainer.upper()}! There are 3 POKEMON here! Ha ha!
When I was young, I was a serious POKEMON trainer.
In my old age, I have only 3 left, but you can have one! Choose!\n""")
                break

    def valid_initial_pokemon(self):
        initial_poke = ""
        initial_pokes = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
        while initial_poke not in initial_pokes:
            initial_poke = input("> ").capitalize()
            if initial_poke not in initial_pokes:
                print("Enter a right pokemon:")
    
        print(Art.POKEMONS[initial_poke])
        print("\n \n")
        self.poke = Pokemon(initial_poke)
        self.current_stats = self.poke.increase_stats()

    def print_welcome(self):
        print(Art.POKEMONS["Pikachu"])
        print("""
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$##$##$##$ ---          Pokemon            --- #$##$##$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$# \n""")
        
        Validations.choose_difficulty(self)
        
        print("""
Hello there! Welcome to the world of POKEMON! My name is OAK!")
People call me the POKEMON PROF! \n
This world is inhabited by creatures called POKEMON! For some
people, POKEMON are pets. Others use them for fights. Myself...
I study POKEMON as a profession.\n
First, what is your name?""")
    
        Validations.valid_trainer_name(self)
        initial_pokes = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
        for index, poke in enumerate(initial_pokes):
            if poke != "Pikachu":
                print(f"{index + 1}.", poke.capitalize(), end= "    ")
            else:
                print("")
        Validations.valid_initial_pokemon(self)
        print(f"You selected {self.poke.poke_info['species'].upper()}. Great choice!")
        print("Give your pokemon a name?")
        self.initial_poke_name = input("> ")
        if self.initial_poke_name == "":
            self.initial_poke_name = self.initial_poke 
        self.poke.name = self.initial_poke_name
        print(f"{self.name_trainer.upper()}, raise your young {self.initial_poke_name.upper()} by making it fight!")
        print("When you feel ready you can challenge BROCK, the PEWTER's GYM LEADER")
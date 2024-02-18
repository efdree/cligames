from pokedex.pokemons import Pokedex
import random
import math

class Pokemon:
    
    def __init__(self, species):
        self.name = ""
        self.poke_info = Pokedex.POKEMONS[species]
        self.growth_rate = self.poke_info["growth_rate"]
        self.current_stats = {}
        self.individual_values = Pokemon.generate_values(31)
        self.level = 1
        self.effort_values = Pokemon.generate_values(0)
        self.base_values = self.poke_info["base_stats"]
        self.remaining_experience = 0
        self.total_experience = 0
        self.exp_to_next_lvl = Pokemon.calculate_next_level(self)
                
        
    def generate_values(value):        
        stats = {
            "hp" : random.randint(0,value),
            "attack" : random.randint(0,value),
            "defense" : random.randint(0,value),
            "special_attack" : random.randint(0,value),
            "special_defense" : random.randint(0,value),
            "speed" : random.randint(0,value)
        }
        
        return stats

    def prepare_for_battle():
        return None
    
    def receive_damage():
        return None
    
    def set_current_move(self):
        current_move = ""
        poke_moves = self.poke_info["moves"]
        for index, move in enumerate(poke_moves, 1):
            print(f"{index}. {move.capitalize()}    ", end="")
        print("")
        while current_move == "" or current_move not in poke_moves:
            current_move = input("> ").lower()
            if current_move in poke_moves:
                continue
        print("-"*50)
        return current_move
    
    def fainted():
        return None
    
    def increase_level(self, gain_experience):
        gain_experience += self.remaining_experience
        cont = 0
        while gain_experience > cont:
            cont = Pokemon.calculate_next_level(self)
            if gain_experience > cont:
                self.level += 1
                print(f"{self.name} reached level {self.level}")
                gain_experience -= cont
            cont = Pokemon.calculate_next_level(self)
        self.remaining_experience = gain_experience
        self.exp_to_next_lvl = cont - self.remaining_experience
        return self.exp_to_next_lvl
        
    def calculate_next_level(self):
        to_new_level = 0
        if self.growth_rate == "slow":
            to_new_level = (((5 * ((self.level +1)**3))) / 4.0).__round__(0)
        elif self.growth_rate == "medium_slow":
            a = ((6 * ((self.level + 1)**3)) / 5.0)
            b = ((15 * ((self.level + 1)**2)))
            c = (100 * (self.level + 1))
            to_new_level = (a - b + c - 140).__round__(0)
        elif self.growth_rate == "medium_fast":
            to_new_level = (self.level + 1)**3
        elif self.growth_rate == "fast":
            to_new_level = ((4 * ((self.level + 1)**3)) / 5.0).__round__(0)
            
        return to_new_level
    
    def increase_effort_values(self, target):
        info = target.poke_info["effort_points"]
        type = info["type"]
        amount = info["amount"]
        self.effort_values[type] += amount
        return self.effort_values
    
    def increase_stats(self,target = ""):
        if target != "":
            Pokemon.increase_effort_values(self,target)
        keys = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]
        stat_values = []
        for key in keys:
            const = self.level + 10 if key == "hp" else 5
            a = (2 * self.base_values[key])
            stat_value = math.floor(((a + self.individual_values[key] + self.effort_values[key]) * self.level / 100) + const)
            stat_values.append(stat_value)
        hash = dict(zip(keys, stat_values))
        self.current_stats = hash
        return self.current_stats
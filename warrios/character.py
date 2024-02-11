from catalog.characters import Catalog as Characters
import random

class Character:
    def __init__(self, name, type):
        char_details = Characters.CHARACTERS[type]
        self.name = name
        self.type = type
        self.experience = char_details["base_exp"]
        self.max_health = char_details["base_stats"]["hp"]
        self.speed = char_details["base_stats"]["speed"]
        self.moves = char_details["moves"]
        self.health = None
        self.current_move = None
    
    def prepare_for_battle(self):
        self.health = self.max_health
        self.current_move = None

    def receive_damage(self, damage):
        self.health -= damage

    def fainted(self):
        return not self.health > 0

    def attack(self, character):
        random_number = random.randint(1,100)
        hits = self.current_move["accuracy"] >= random_number
        print(f"{self.name} uses {self.current_move['name']}")
        if hits:
            character.receive_damage(self.current_move["power"])
            print(f"Hits {character.name} and caused {self.current_move['power']} damage")
        else:
            print(f"{self.name} failed to hit {character.name} and didn't couse any damage")
    
    def increase_experience(self, character):
        self.experience += character.experience * 0.2



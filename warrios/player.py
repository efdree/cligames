from catalog.characters import Catalog as Characters
from catalog.moves import Catalog as Moves
import random

class Player:
    def __init__(self, name, character_type, character_name):
        self.name = name
        self.character = Characters.new(character_name, character_type)
    
    def select_move(self):
        move = input("Select a move to attack", self.character.moves)
        self.character.current_move = Moves.MOVES[move]

class Bot(Player):
    def __init__(self):
        characterForBot = {name: data for name, data in Characters.CHARACTERS.items() if data["type"] == "bot"}
        selected_character = random.choice(list(characterForBot.keys()))
        super().__init__("Dragon Master", selected_character, selected_character.capitalize())
        
    def select_move(self):
        move = random.choice(self.character.moves)
        self.character.current_move = Moves.MOVES[move]


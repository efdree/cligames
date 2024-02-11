from catalog.characters import Catalog as Characters
from catalog.moves import Catalog as Moves
from character import Character
from get_input import get_with_options
import random

class Player:
    def __init__(self, name, character_name, character_type):
        self.name = name
        self.character = Character(character_type, character_name)
    
    def select_move(self):
        move = get_with_options("Select a move to attack", self.character.moves)
        self.character.current_move = Moves.MOVES[move]

class Bot(Player):
    def __init__(self):
        characterForBot = {name: data for name, data in Characters.CHARACTERS.items() if data["type"] == "bot"}
        selected_character = random.choice(list(characterForBot.keys()))
        super().__init__("Dragon Master", selected_character, selected_character.capitalize())
        
    def select_move(self):
        move = random.choice(self.character.moves)
        self.character.current_move = Moves.MOVES[move]


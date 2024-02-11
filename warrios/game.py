from catalog.characters import Catalog as Characters
from player import Player, Bot
from battle import Battle
from get_input import get_with_options, validate_input

def select_character():
    names = [name for name, data in Characters.CHARACTERS.items() if data["type"] == "player"] 
    return get_with_options("Choose a character:", names)

user = ""
while user == "":
    user = validate_input("What's is your name?")

character = select_character()
character_name = validate_input("Give your character a name:")
player = Player(user, character, character_name)
bot = Bot()
battle = Battle(player, bot)
battle.start()

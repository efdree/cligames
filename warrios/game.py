from catalog.characters import Catalog as Characters
from catalog.moves import Catalog as Moves
import random

user = ""
while user == "":
    print("What's is your name? ")
    user = input("> ").lower()

print("Choose a character: ")

characterForPlayer = {name: data for name, data in Characters.CHARACTERS.items() if data["type"] == "player"}

characterForBot = {name: data for name, data in Characters.CHARACTERS.items() if data["type"] == "bot"}

countCharPlayer = 0
for character in characterForPlayer:
    countCharPlayer += 1
    print(f"{countCharPlayer}. {character}")

characterPlayer = ""
while characterPlayer not in characterForPlayer:
    if characterPlayer != "": print("Insert a Right Character")
    characterPlayer = input("> ").lower()
print("Give your character a name: ")
nameCharacter = input("> ")

characterBot = random.choice(list(characterForBot.items()))

print("-"*20)
print(f"{user} challenges Dragon Master to a battle.")
print(f"{user} use {characterPlayer.capitalize()}")
print(f"Dragon Master uses {characterBot[0].capitalize()}")
print("-"*20)

print("Select a move to attack")

for name, data in characterForPlayer.items():
    if name == characterPlayer:
        movesByPlayer = data["moves"]

countMovPlayer = 0
for move in movesByPlayer:
    countMovPlayer +=1
    print(f"{countMovPlayer}. {move}")

movePlayer = ""
while movePlayer not in movesByPlayer:
    if movePlayer != "" : print("Insert a Right Move")
    movePlayer = input("> ").lower()

movesByBot = characterBot[1]["moves"]

moveBot = random.choice(movesByBot)

print("-"*20)
print(f"{characterBot[0].capitalize()} use {moveBot}")
print(f"Hits {nameCharacter} and caused 4 damage")
print(f"{nameCharacter} uses {movePlayer}")
print(f"Hits {characterBot[0].capitalize()} and caused 40 damage")
print("-"*20)


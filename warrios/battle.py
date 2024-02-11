import random

class Battle:
    
    def __init__(self, player, bot):
        self.player = player
        self.bot = bot
        self.player_char = self.player.character
        self.bot_char = self.bot.character
        
    def announce(self):
        print("-"*20)
        print(f"{self.player.name.capitalize()} challenges {self.bot.name} to a battle.")
        print(f"{self.player.name.capitalize()} use {self.player_char.name.capitalize()}")
        print(f"{self.bot.name} uses {self.bot_char.name.capitalize()}")
        print("-"*20)
        
    def start(self):
        self.player_char.prepare_for_battle()
        self.bot_char.prepare_for_battle()
        Battle.announce(self)
        while not self.player_char.fainted() and not self.bot_char.fainted():
            self.player.select_move()
            self.bot.select_move()
            first = Battle.select_first(self.player_char, self.bot_char)
            second = self.bot_char if first == self.player_char else self.player_char
            print("-"*20)
            first.attack(second)
            if not second.fainted():
                second.attack(first)
            print("-"*20)
            
        winner = self.bot_char if not self.player_char.fainted() else self.player_char    
        loser = self.bot_char if winner == self.player_char else self.player_char
        
        winner.increase_experience(loser)
        print(f"{winner.name.capitalize()} WINS! They experience reached {winner.experience} points.")
        
    def select_first(player_char, bot_char):
        player_move = player_char.current_move
        bot_move = bot_char.current_move
        if player_move["priority"] > bot_move["priority"]:
            return player_char
        elif player_move["priority"] < bot_move["priority"]:
            return bot_char
        
        if player_char.speed > bot_char.speed:
            return player_char
        elif player_char.speed < bot_char.speed:
            return bot_char
        
        return random.choice([player_char, bot_char])
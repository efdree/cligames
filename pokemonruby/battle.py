from pokedex.moves import Pokedex as MOVES
from pokedex.moves import SPECIAL_MOVE_TYPE, TYPE_MULTIPLIER
import random
import math

class Battle:
    
    def __init__(self, trainer, poke, o_trainer, opponent):
        self.win = False
        self.trainer = trainer
        self.poke = poke
        self.o_trainer = o_trainer
        self.opponent = opponent
        
    def start(self):
        poke_hp = self.poke.current_stats["hp"]
        opponent_hp = self.opponent.current_stats["hp"]
        while opponent_hp > 0 and poke_hp > 0:
            moves = Battle.choosing_moves(self)
            move = moves[0]
            o_move = moves[1]
            first = Battle.who_goes_first(self,move, o_move)
            if first == self.poke:
                f_remaining_hp = poke_hp
                s_remaining_hp = opponent_hp
                opponent_hp = Battle.attacks(self, move, self.poke, self.opponent, s_remaining_hp)
                if opponent_hp > 0:
                    poke_hp = Battle.attacks(self, o_move, self.opponent, self.poke, f_remaining_hp)
            else:
                s_remaining_hp = poke_hp
                f_remaining_hp = opponent_hp
                poke_hp = Battle.attacks(self, o_move, self.opponent, self.poke, s_remaining_hp)
                if poke_hp > 0:
                    opponent_hp = Battle.attacks(self, move, self.poke, self.opponent, f_remaining_hp)
        return Battle.who_won(self, poke_hp)
        
    def who_won(self,poke_hp):
        if poke_hp > 0:
            winner = self.poke
        else:
            winner = self.opponent
        return Battle.winner_messages(self,winner)
    
    def winner_messages(self, winner):
        if winner == self.poke:
            print(f"{self.opponent.name.upper()} FAINTED!")
            print("--------------------------------------------------")        
            print(f"{self.poke.name.upper()} WINS!")
            base_exp = self.opponent.poke_info["base_exp"]
            gain_experience = math.floor(base_exp * self.opponent.level / 7)
            self.poke.total_experience += gain_experience
            print(f"{self.poke.name.upper()} gained {gain_experience} experience points")
            print("------------------Battle Ended!-------------------")
            self.poke.increase_level(gain_experience)
            self.poke.increase_stats(self.opponent)
            self.win = True
            if self.opponent == "Brock":
                print("Congratulations! You win the BOULDER BADGE.")
        else:
            print(f"{self.poke.name.capitalize()} FAINTED!")
            print("--------------------------------------------------")        
            print(f"{self.opponent.name.capitalize()} WINS!")
            print("------------------Battle Ended!-------------------")
            
    def attacks(self, move, attacker, attacked, current_hp):
        print(f"{attacker.name.capitalize()} used {move.upper()}!")
        if Battle.check_accuracy(self,move) == True:
            factor = 1.5 if Battle.critical_hit() else 1
            multiplier = Battle.how_much_effective(self,move, attacker)
            damage = Battle.calculate_damage(self,move, attacker)
            final_damage = math.floor(damage * factor * multiplier)
            current_hp -= final_damage
            print(f"And it hit {attacked.name.upper()} with {final_damage} damage")
            print("--------------------------------------------------")        
            return current_hp
        else:
            return attacked.current_stats["hp"]
    
    def choosing_moves(self):
        o_poke_moves = self.opponent.poke_info["moves"]
        o_move = random.choice(o_poke_moves)
        print(f"{self.trainer.upper()}, select your move:")
        move = self.poke.set_current_move()
        return [move, o_move]
    
    def who_goes_first(self,move, o_move):
        o_priority = MOVES.MOVES[o_move]["priority"]
        o_speed = self.opponent.current_stats["speed"]
        priority = MOVES.MOVES[move]["priority"]
        speed = self.poke.current_stats["speed"]

        if o_priority != priority:
            first = self.opponent if o_priority > priority else self.poke
        elif o_speed != speed:
            first = self.opponent if o_speed > speed else self.poke
        else:
            options = [self.poke, self.opponent]
            first = options[random.randint(0,1)]
        return first
  
    def check_accuracy(self,move):
        accuracy = MOVES.MOVES[move]["accuracy"]
        if accuracy == 100:
            return True
        else:
            limit = (100.0 / (100 - accuracy)).__round__(0)
            n = random.randint(1,limit)
            if n == 1:
                print(f"{move.upper()} has failed")
            else:
                return True

    def critical_hit():
        n = random.randint(1,16)
        if n == 1:
            print("It was a CRITICAL HIT!")
            return True
        else:
            return False

    def how_much_effective(self,move, first):
        second = self.opponent if first == self.poke else self.poke
        f_type = MOVES.MOVES[move]["type"]
        s_type = second.poke_info["type"]
        arr = TYPE_MULTIPLIER
        multiplier = 1
        for hash in arr:
            for i in range(0,len(s_type) - 1):
                if hash["user"] == f_type and hash["target"] == s_type[i]:
                    multiplier = hash["multiplier"] * multiplier
        Battle.string_multiplier(multiplier)
        return multiplier

    def string_multiplier(multiplier):
        if multiplier == 0:
            print("It's not effective at all")
        elif multiplier >= 0.1 and multiplier <= 0.5:
            print("It's not very effective...")
        elif multiplier >= 0.6 and multiplier <= 1:
            print("It's a normal attack")
        elif multiplier >= 1.1 and multiplier <= 4:
            print("It's super effective!")
        
    def calculate_damage(self, move, attacker):
        attacked = self.opponent if attacker == self.poke else self.poke
        level = attacker.level
        move_type = MOVES.MOVES[move]["type"]
        special_moves = SPECIAL_MOVE_TYPE
        if move_type in special_moves:
            offensive_stat = attacker.current_stats["special_attack"]
            target_defensive_stat = attacked.current_stats["special_defense"]
        else:
            offensive_stat = attacker.current_stats["attack"]
            target_defensive_stat = attacked.current_stats["defense"]
    
        move_power = MOVES.MOVES[move]["power"]
        return math.floor(math.floor(math.floor((2 * level / 5.0) + 2) * offensive_stat * move_power / target_defensive_stat) / 50.0) + 2
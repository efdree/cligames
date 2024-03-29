class Pokedex:
    POKEMONS = {
        "Bulbasaur": {
            "species": "Bulbasaur",
            "type": ["grass", "poison"],
            "base_exp": 64,
            "effort_points": {"type": "special_attack", "amount": 1},
            "growth_rate": "slow",
            "base_stats": {"hp": 45, "attack": 49, "defense": 49, "special_attack": 65, "special_defense": 65, "speed": 45},
            "moves": ["tackle", "vine whip"]
        },
        "Charmander": {
            "species": "Charmander",
            "type": ["fire"],
            "base_exp": 62,
            "effort_points": {"type": "speed", "amount": 1},
            "growth_rate": "medium_slow",
            "base_stats": {"hp": 39, "attack": 52, "defense": 43, "special_attack": 60, "special_defense": 50, "speed": 65},
            "moves": ["scratch", "ember"]
        },
        "Squirtle": {
            "species": "Squirtle",
            "type": ["water"],
            "base_exp": 63,
            "effort_points": {"type": "defense", "amount": 1},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 44, "attack": 48, "defense": 65, "special_attack": 50, "special_defense": 64, "speed": 43},
            "moves": ["tackle", "bubble"]
        },
        "Ratata": {
            "species": "Ratata",
            "type": ["normal"],
            "base_exp": 51,
            "effort_points": {"type": "speed", "amount": 1},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 30, "attack": 56, "defense": 35, "special_attack": 25, "special_defense": 35, "speed": 72},
            "moves": ["tackle", "quick attack"]
        },
        "Spearow": {
            "species": "Spearow",
            "type": ["normal", "flying"],
            "base_exp": 52,
            "effort_points": {"type": "speed", "amount": 1},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 40, "attack": 60, "defense": 30, "special_attack": 31, "special_defense": 31, "speed": 70},
            "moves": ["peck", "persuit"]
        },
        "Pikachu": {
            "species": "Pikachu",
            "type": ["electric"],
            "base_exp": 112,
            "effort_points": {"type": "speed", "amount": 2},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 35, "attack": 55, "defense": 40, "special_attack": 50, "special_defense": 50, "speed": 90},
            "moves": ["thunder shock", "quick attack", "iron tail"]
        },
        "Onix": {
            "species": "Onix",
            "type": ["rock", "ground"],
            "base_exp": 77,
            "effort_points": {"type": "defense", "amount": 1},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 35, "attack": 45, "defense": 160, "special_attack": 30, "special_defense": 45, "speed": 70},
            "moves": ["tackle", "rock throw"]
        },
        "Mewtwo": {
            "species": "Mewtwo",
            "type": ["psychic"],
            "base_exp": 120,
            "effort_points": {"type": "special_attack", "amount": 3},
            "growth_rate": "medium_fast",
            "base_stats": {"hp": 106, "attack": 110, "defense": 90, "special_attack": 154, "special_defense": 90, "speed": 130},
            "moves": ["persuit", "confusion"]
        },
        "Machop": {
            "species": "Machop",
            "type": ["fighting"],
            "base_exp": 61,
            "effort_points": {"type": "attack", "amount": 1 },
            "growth_rate": "medium_slow",
            "base_stats": { "hp": 70, "attack": 80, "defense": 50, "special_attack": 35, "special_defense": 35, "speed": 35 },
            "moves": ["high jump kick", "tackle"]
        },
        "Jigglypuff" : {
            "species": "Jigglypuff",
            "type": ["fairy", "normal"],
            "base_exp": 95,
            "effort_points": { "type": "hp", "amount": 2 },
            "growth_rate": "fast",
            "base_stats": { "hp": 115, "attack": 45, "defense": 20, "special_attack": 45, "special_defense": 25, "speed": 20 },
            "moves": ["play rough", "confusion"]
        }
    }
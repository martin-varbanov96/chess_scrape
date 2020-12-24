# transform_data.py
import json

GAMES = "games"

def to_pgn(input_json):
    json_strucutre = dict()
    with open(input_json, "r") as f:
        contents = f.read()
        json_structure = json.loads(contents)
    
    for game in json_structure[GAMES]:
        unique_id = game['url'].split("/")[-1]
        # TODO: add directory functionality
        full_name = f"{unique_id}.pgn"
        with open(full_name, "w") as f:
            f.write(game["pgn"])

to_pgn("202012_games.json")        

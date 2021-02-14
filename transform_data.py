# transform_data.py
import json

GAMES = "games"


# sample entry in json:
# {"url": "https://www.chess.com/live/game/6110029835","pgn": "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2020.12.31\"]\n[Round \"-\"]\n[White \"Jeremy249\"]\n[Black \"funvengeance\"]\n[Result \"1-0\"]\n[CurrentPosition \"r2q1rk1/1b2b1p1/4Np2/2n3P1/1p5Q/p4P2/PPP5/1K5R b - -\"]\n[Timezone \"UTC\"]\n[ECO \"B95\"]\n[ECOUrl \"https://www.chess.com/openings/Sicilian-Defense-Open-Najdorf-Variation-6.Bg5-e6-7.Qe2\"]\n[UTCDate \"2020.12.31\"]\n[UTCTime \"22:36:42\"]\n[WhiteElo \"1293\"]\n[BlackElo \"1216\"]\n[TimeControl \"60+1\"]\n[Termination \"Jeremy249 won on time\"]\n[StartTime \"22:36:42\"]\n[EndDate \"2020.12.31\"]\n[EndTime \"22:39:09\"]\n[Link \"https://www.chess.com/live/game/6110029835\"]\n\n1. e4 {[%clk 0:01:01]} 1... c5 {[%clk 0:01:00.4]} 2. Nf3 {[%clk 0:01:00.3]} 2... d6 {[%clk 0:01:00.9]} 3. d4 {[%clk 0:01:00.2]} 3... cxd4 {[%clk 0:01:01.8]} 4. Nxd4 {[%clk 0:01:01]} 4... Nf6 {[%clk 0:01:02.4]} 5. Nc3 {[%clk 0:01:00.2]} 5... a6 {[%clk 0:01:02.4]} 6. Bg5 {[%clk 0:00:59.6]} 6... e6 {[%clk 0:01:02.2]} 7. Qe2 {[%clk 0:00:57.7]} 7... Be7 {[%clk 0:01:01]} 8. O-O-O {[%clk 0:00:57.5]} 8... b5 {[%clk 0:00:58.3]} 9. e5 {[%clk 0:00:56.4]} 9... dxe5 {[%clk 0:00:58.1]} 10. Qxe5 {[%clk 0:00:56.1]} 10... Nbd7 {[%clk 0:00:57.2]} 11. Qe3 {[%clk 0:00:52]} 11... Bb7 {[%clk 0:00:57]} 12. h4 {[%clk 0:00:51.5]} 12... O-O {[%clk 0:00:54.8]} 13. Rg1 {[%clk 0:00:51]} 13... h6 {[%clk 0:00:54.1]} 14. Bf4 {[%clk 0:00:50.3]} 14... b4 {[%clk 0:00:50.9]} 15. Ne4 {[%clk 0:00:49.5]} 15... Nxe4 {[%clk 0:00:43.8]} 16. Bd3 {[%clk 0:00:48.5]} 16... Ndf6 {[%clk 0:00:43.7]} 17. f3 {[%clk 0:00:47.9]} 17... Nc5 {[%clk 0:00:35.6]} 18. Be2 {[%clk 0:00:44.6]} 18... a5 {[%clk 0:00:34.6]} 19. g4 {[%clk 0:00:44.4]} 19... a4 {[%clk 0:00:30.9]} 20. g5 {[%clk 0:00:44.3]} 20... hxg5 {[%clk 0:00:28.1]} 21. hxg5 {[%clk 0:00:43.3]} 21... Nd5 {[%clk 0:00:26.9]} 22. Qf2 {[%clk 0:00:43.3]} 22... Nxf4 {[%clk 0:00:26.8]} 23. Qh4 {[%clk 0:00:43.3]} 23... Nxe2+ {[%clk 0:00:26.7]} 24. Kb1 {[%clk 0:00:41.6]} 24... Nxg1 {[%clk 0:00:27.6]} 25. Rxg1 {[%clk 0:00:41.7]} 25... a3 {[%clk 0:00:26.4]} 26. Rh1 {[%clk 0:00:40.7]} 26... f6 {[%clk 0:00:02.6]} 27. Nxe6 {[%clk 0:00:39.7]} 1-0", "time_control": "60+1", "end_time": 1609454349, "rated": true, "fen": "r2q1rk1/1b2b1p1/4Np2/2n3P1/1p5Q/p4P2/PPP5/1K5R b - -", "time_class": "bullet", "rules": "chess", "white": {"rating": 1293, "result": "win", "@id": "https://api.chess.com/pub/player/jeremy249", "username": "Jeremy249"}, "black": {"rating": 1216, "result": "timeout", "@id": "https://api.chess.com/pub/player/funvengeance", "username": "funvengeance"}}


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
   
# to_pgn("202012_games.json")        
entry = {"url": "https://www.chess.com/live/game/6110029835",
         "pgn": "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2020.12.31\"]\n[Round \"-\"]\n[White \"Jeremy249\"]\n[Black \"funvengeance\"]\n[Result \"1-0\"]\n[CurrentPosition \"r2q1rk1/1b2b1p1/4Np2/2n3P1/1p5Q/p4P2/PPP5/1K5R b - -\"]\n[Timezone \"UTC\"]\n[ECO \"B95\"]\n[ECOUrl \"https://www.chess.com/openings/Sicilian-Defense-Open-Najdorf-Variation-6.Bg5-e6-7.Qe2\"]\n[UTCDate \"2020.12.31\"]\n[UTCTime \"22:36:42\"]\n[WhiteElo \"1293\"]\n[BlackElo \"1216\"]\n[TimeControl \"60+1\"]\n[Termination \"Jeremy249 won on time\"]\n[StartTime \"22:36:42\"]\n[EndDate \"2020.12.31\"]\n[EndTime \"22:39:09\"]\n[Link \"https://www.chess.com/live/game/6110029835\"]\n\n1. e4 {[%clk 0:01:01]} 1... c5 {[%clk 0:01:00.4]} 2. Nf3 {[%clk 0:01:00.3]} 2... d6 {[%clk 0:01:00.9]} 3. d4 {[%clk 0:01:00.2]} 3... cxd4 {[%clk 0:01:01.8]} 4. Nxd4 {[%clk 0:01:01]} 4... Nf6 {[%clk 0:01:02.4]} 5. Nc3 {[%clk 0:01:00.2]} 5... a6 {[%clk 0:01:02.4]} 6. Bg5 {[%clk 0:00:59.6]} 6... e6 {[%clk 0:01:02.2]} 7. Qe2 {[%clk 0:00:57.7]} 7... Be7 {[%clk 0:01:01]} 8. O-O-O {[%clk 0:00:57.5]} 8... b5 {[%clk 0:00:58.3]} 9. e5 {[%clk 0:00:56.4]} 9... dxe5 {[%clk 0:00:58.1]} 10. Qxe5 {[%clk 0:00:56.1]} 10... Nbd7 {[%clk 0:00:57.2]} 11. Qe3 {[%clk 0:00:52]} 11... Bb7 {[%clk 0:00:57]} 12. h4 {[%clk 0:00:51.5]} 12... O-O {[%clk 0:00:54.8]} 13. Rg1 {[%clk 0:00:51]} 13... h6 {[%clk 0:00:54.1]} 14. Bf4 {[%clk 0:00:50.3]} 14... b4 {[%clk 0:00:50.9]} 15. Ne4 {[%clk 0:00:49.5]} 15... Nxe4 {[%clk 0:00:43.8]} 16. Bd3 {[%clk 0:00:48.5]} 16... Ndf6 {[%clk 0:00:43.7]} 17. f3 {[%clk 0:00:47.9]} 17... Nc5 {[%clk 0:00:35.6]} 18. Be2 {[%clk 0:00:44.6]} 18... a5 {[%clk 0:00:34.6]} 19. g4 {[%clk 0:00:44.4]} 19... a4 {[%clk 0:00:30.9]} 20. g5 {[%clk 0:00:44.3]} 20... hxg5 {[%clk 0:00:28.1]} 21. hxg5 {[%clk 0:00:43.3]} 21... Nd5 {[%clk 0:00:26.9]} 22. Qf2 {[%clk 0:00:43.3]} 22... Nxf4 {[%clk 0:00:26.8]} 23. Qh4 {[%clk 0:00:43.3]} 23... Nxe2+ {[%clk 0:00:26.7]} 24. Kb1 {[%clk 0:00:41.6]} 24... Nxg1 {[%clk 0:00:27.6]} 25. Rxg1 {[%clk 0:00:41.7]} 25... a3 {[%clk 0:00:26.4]} 26. Rh1 {[%clk 0:00:40.7]} 26... f6 {[%clk 0:00:02.6]} 27. Nxe6 {[%clk 0:00:39.7]} 1-0",
         "time_control": "60+1",
         "end_time": 1609454349,
         "rated": True,
         "fen": "r2q1rk1/1b2b1p1/4Np2/2n3P1/1p5Q/p4P2/PPP5/1K5R b - -",
         "time_class": "bullet",
         "rules": "chess", 
         "white": {"rating": 1293,"result": "win", "@id": "https://api.chess.com/pub/player/jeremy249", "username": "Jeremy249"}, 
         "black": {"rating": 1216, "result": "timeout", "@id": "https://api.chess.com/pub/player/funvengeance", "username": "funvengeance"}}
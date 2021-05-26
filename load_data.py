# load_data.py
import mysql.connector
from mysql.connector.errors import IntegrityError, OperationalError
from PersonalVariables import personal_variables as pv
import pymongo

class DataLoader:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(pv.mongo_connection)
        self.mongodb = self.mongo_client[pv.cloud_mongo_db]
        self.mysql_db = mysql.connector.connect(host=pv.mysql_aws_host,
                                                user=pv.mysql_aws_user,
                                                password=pv.mysql_aws_password,
                                                database=pv.mysql_aws_database)

        self.mysql_cursor = self.mysql_db.cursor()


    def mongo_many_insert_to_collection(self, collection, docs_list):
        assert(type(docs_list) == list)
        assert(type(collection) == str)
        col = self.mongodb[collection]
        # status = col.insert_many(docs_list)
        for doc in docs_list:
            status = col.update_one(doc, {"$set": doc}, upsert=True)
            # TODO: improve logging
            if(status.modified_count == 0):
                print(f"element {doc['url']} was not inserted")

    def mysql_insert_player(self, player_username):
            # what happens if adding fails ?
            insert_player_username_val = player_username,
            insert_player_username_sql = "INSERT INTO all_chess_games_chessplayer(username) VALUES (%s)"
            try:
                self.mysql_cursor.execute(insert_player_username_sql, insert_player_username_val)
            except IntegrityError:
                # username already in db
                return
            except OperationalError:
                #  TODO: mysql connection was lost try reconnecting
                return
            self.mysql_db.commit()
            print("1 record inserted, id:", self.mysql_cursor.lastrowid)

    def mysql_select_player_id(self, player_username):
        # player_username_val = player_username,
        player_id_q = f"select id from all_chess_games_chessplayer where username='{player_username}'"
        self.mysql_cursor.execute(player_id_q)
        user_id = self.mysql_cursor.fetchall()

        if(user_id ==[] or len(user_id) > 1 or user_id[0]== ()):
            return None
        return user_id[0][0]

    def mysql_many_insert(self, input_games):
        # {'url': 'https://www.chess.com/game/live/11013774491', 
        # 'pgn': '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2021.04.01"]\n[Round "-"]\n[White "funvengeance"]\n[Black "forrie"]\n[Result "1-0"]\n[CurrentPosition "r3r1k1/3nqpPp/2p5/p2p4/1p1PN3/3Q4/PPP1NPP1/2KR3R b - -"]\n[Timezone "UTC"]\n[ECO "B07"]\n[ECOUrl "https://www.chess.com/openings/Pirc-Defense-2.d4-Nf6-3.Nc3"]\n[UTCDate "2021.04.01"]\n[UTCTime "10:56:39"]\n[WhiteElo "1269"]\n[BlackElo "1317"]\n[TimeControl "120+1"]\n[Termination "funvengeance won on time"]\n[StartTime "10:56:39"]\n[EndDate "2021.04.01"]\n[EndTime "11:01:25"]\n[Link "https://www.chess.com/game/live/11013774491"]\n\n1. e4 {[%clk 0:02:01]} 1... d6 {[%clk 0:02:00.9]} 2. d4 {[%clk 0:02:00.5]} 2... Nf6 {[%clk 0:02:00.9]} 3. Nc3 {[%clk 0:02:00.6]} 3... e5 {[%clk 0:01:55.5]} 4. Bg5 {[%clk 0:01:56]} 4... Nbd7 {[%clk 0:01:42.1]} 5. Nf3 {[%clk 0:01:55.4]} 5... c6 {[%clk 0:01:37]} 6. Qd2 {[%clk 0:01:51.1]} 6... Be7 {[%clk 0:01:34.2]} 7. Bd3 {[%clk 0:01:46.9]} 7... O-O {[%clk 0:01:33.8]} 8. O-O-O {[%clk 0:01:45.9]} 8... b5 {[%clk 0:01:25]} 9. h4 {[%clk 0:01:44.8]} 9... b4 {[%clk 0:01:23.2]} 10. Ne2 {[%clk 0:01:43.9]} 10... a5 {[%clk 0:01:22.3]} 11. h5 {[%clk 0:01:43.8]} 11... Ba6 {[%clk 0:01:08.6]} 12. Bxa6 {[%clk 0:01:39.6]} 12... Nxe4 {[%clk 0:01:07]} 13. Bxe7 {[%clk 0:01:29]} 13... Qxe7 {[%clk 0:00:51.7]} 14. Qe3 {[%clk 0:01:09.1]} 14... d5 {[%clk 0:00:37.6]} 15. Bd3 {[%clk 0:01:03.7]} 15... Nef6 {[%clk 0:00:25.4]} 16. h6 {[%clk 0:00:47.8]} 16... e4 {[%clk 0:00:22.1]} 17. hxg7 {[%clk 0:00:39.6]} 17... Rfe8 {[%clk 0:00:21.7]} 18. Ng5 {[%clk 0:00:08.8]} 18... exd3 {[%clk 0:00:16.8]} 19. Qxd3 {[%clk 0:00:04.4]} 19... Ne4 {[%clk 0:00:05.1]} 20. Nxe4 {[%clk 0:00:03.6]} 1-0\n',
        # 'time_control': '120+1', 'end_time': 1617274885, 'rated': True,
        # 'fen': 'r3r1k1/3nqpPp/2p5/p2p4/1p1PN3/3Q4/PPP1NPP1/2KR3R b - -', 'time_class': 'bullet', 
        # 'rules': 'chess',
        # 'white': {'rating': 1269, 'result': 'win', '@id': 'https://api.chess.com/pub/player/funvengeance', 'username': 'funvengeance'},
        # 'black': {'rating': 1317, 'result': 'timeout', '@id': 'https://api.chess.com/pub/player/forrie', 'username': 'forrie'}}

        # TODO: maybe add a seperate exception for both cases
        if(type(input_games) != list or input_games == []):
            print("no games were added")
            return 
        for current_game in input_games:
            white_username = current_game['white']['username']
            black_username = current_game['black']['username']

            # inserting usernames into db
            self.mysql_insert_player(white_username)
            self.mysql_insert_player(black_username)
            
            game_url = str(current_game['url'])
            game_pgn = str(current_game['pgn'])
            game_time_control = str(current_game['time_control'])
            game_white_rating = int(current_game['white']['rating'])
            game_white_result = str(current_game['white']['result'])
            game_black_rating = int(current_game['black']['rating'])
            game_black_result = str(current_game['black']['result'])
            game_white_player_id = self.mysql_select_player_id(white_username)
            game_black_player_id = self.mysql_select_player_id(black_username)

            if(game_white_player_id and game_black_player_id):
                game_white_player_id = int(game_white_player_id)
                game_black_player_id = int(game_black_player_id)
                insert_games_sql = "INSERT INTO all_chess_games_chessgame (url, pgn, time_class, white_rating, white_result, black_rating, black_result, black_player_id, white_player_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert_games_val = (game_url,
                                    game_pgn,
                                    game_time_control,
                                    game_white_rating,
                                    game_white_result,
                                    game_black_rating,
                                    game_black_result,
                                    game_white_player_id,
                                    game_black_player_id,)

                try:
                    self.mysql_cursor.execute(insert_games_sql, insert_games_val)
                except IntegrityError:
                    # username already in db
                    continue
                except OperationalError:
                    #  TODO: mysql connection was lost try reconnecting
                    print("mysql connection lost")
        
                # save result
                self.mysql_db.commit()
                print("1 record inserted, ID:", self.mysql_cursor.lastrowid)
            else:
                continue
    


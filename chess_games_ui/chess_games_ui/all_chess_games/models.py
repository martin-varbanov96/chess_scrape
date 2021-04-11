from django.db import models

class ChessPlayer(models.Model):
    id = models.AutoField(primary_key=True,)
    username = models.CharField(max_length=200, null=True)

class ChessGame(models.Model):
    id = models.AutoField(primary_key=True,)
    url = models.CharField(max_length=50, null=True, blank=True)
    pgn = models.CharField(max_length=10000, null=True, blank=True)
    time_class = models.CharField(max_length=50, null=True, blank=True)
    white_player = models.ForeignKey(ChessPlayer,
                                     null=True,
                                     related_name="+",
                                     on_delete= models.SET_NULL)
    white_rating = models.IntegerField(null=True, blank=True)
    white_result = models.CharField(max_length=50, null=True, blank=True)
    black_player = models.ForeignKey(ChessPlayer,
                                     null=True,
                                     related_name="+",
                                     on_delete= models.SET_NULL)
    black_rating = models.IntegerField(null=True, blank=True)
    black_result = models.CharField(max_length=50, null=True, blank=True)

# {'_id': ObjectId('60291ff60907e850a35d22bd'), 
# 'url': 'https://www.chess.com/live/game/6132352376', 
# 'pgn': '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2021.01.03"]\n[Round "-"]\n[White "AdrianoJReis"]\n[Black "funvengeance"]\n[Result "0-1"]\n[CurrentPosition "8/6pp/p3p3/1p4k1/8/PP6/2r5/6bK w - -"]\n[Timezone "UTC"]\n[ECO "B95"]\n[ECOUrl "https://www.chess.com/openings/Sicilian-Defense-Open-Najdorf-Variation-6.Bg5-e6-7.Bd3"]\n[UTCDate "2021.01.03"]\n[UTCTime "15:27:18"]\n[WhiteElo "1204"]\n[BlackElo "1155"]\n[TimeControl "60+1"]\n[Termination "funvengeance won on time"]\n[StartTime "15:27:18"]\n[EndDate "2021.01.03"]\n[EndTime "15:30:30"]\n[Link "https://www.chess.com/live/game/6132352376"]\n\n1. e4 {[%clk 0:00:52.4]} 1... c5 {[%clk 0:00:58.8]} 2. Nf3 {[%clk 0:00:50.4]} 2... d6 {[%clk 0:00:59]} 3. d4 {[%clk 0:00:48.5]} 3... cxd4 {[%clk 0:00:58.4]} 4. Nxd4 {[%clk 0:00:48.2]} 4... Nf6 {[%clk 0:00:58.8]} 5. Nc3 {[%clk 0:00:47.6]} 5... a6 {[%clk 0:00:57.4]} 6. Bg5 {[%clk 0:00:42.9]} 6... e6 {[%clk 0:00:57.2]} 7. Bd3 {[%clk 0:00:36.9]} 7... Be7 {[%clk 0:00:56.9]} 8. O-O {[%clk 0:00:36.6]} 8... O-O {[%clk 0:00:56.5]} 9. Bxf6 {[%clk 0:00:34.6]} 9... Bxf6 {[%clk 0:00:56.2]} 10. Nde2 {[%clk 0:00:35.1]} 10... b5 {[%clk 0:00:54.9]} 11. Rb1 {[%clk 0:00:32.7]} 11... Bb7 {[%clk 0:00:55.3]} 12. f3 {[%clk 0:00:32]} 12... Nd7 {[%clk 0:00:55.5]} 13. Kh1 {[%clk 0:00:31.9]} 13... Qb6 {[%clk 0:00:54.7]} 14. a3 {[%clk 0:00:30.4]} 14... Rac8 {[%clk 0:00:54.1]} 15. Na2 {[%clk 0:00:29.1]} 15... d5 {[%clk 0:00:54.1]} 16. exd5 {[%clk 0:00:27.4]} 16... Bxd5 {[%clk 0:00:53.2]} 17. Nb4 {[%clk 0:00:26.2]} 17... Bb7 {[%clk 0:00:51.3]} 18. Be4 {[%clk 0:00:24.9]} 18... Ne5 {[%clk 0:00:47.2]} 19. Bxb7 {[%clk 0:00:23.9]} 19... Qxb7 {[%clk 0:00:48.1]} 20. Ng3 {[%clk 0:00:22.5]} 20... Rc4 {[%clk 0:00:44.2]} 21. b3 {[%clk 0:00:16.8]} 21... Rc7 {[%clk 0:00:37.8]} 22. Ne4 {[%clk 0:00:15.3]} 22... Be7 {[%clk 0:00:35.5]} 23. Re1 {[%clk 0:00:15.1]} 23... Ng6 {[%clk 0:00:32.9]} 24. Nd3 {[%clk 0:00:13.3]} 24... Rfc8 {[%clk 0:00:30.3]} 25. Ng3 {[%clk 0:00:13]} 25... Rxc2 {[%clk 0:00:29]} 26. Ne5 {[%clk 0:00:10.8]} 26... Nh4 {[%clk 0:00:26.7]} 27. Rc1 {[%clk 0:00:09.5]} 27... Rxg2 {[%clk 0:00:25.4]} 28. Rxc8+ {[%clk 0:00:08.1]} 28... Qxc8 {[%clk 0:00:26.3]} 29. Nxf7 {[%clk 0:00:03.8]} 29... Kxf7 {[%clk 0:00:25.1]} 30. Qd3 {[%clk 0:00:03]} 30... Qc2 {[%clk 0:00:21.8]} 31. Qxc2 {[%clk 0:00:02.3]} 31... Rxc2 {[%clk 0:00:22.7]} 32. Ne4 {[%clk 0:00:02.1]} 32... Nxf3 {[%clk 0:00:22]} 33. Ng5+ {[%clk 0:00:02]} 33... Nxg5 {[%clk 0:00:21.5]} 34. Rf1+ {[%clk 0:00:02]} 34... Kg6 {[%clk 0:00:21.2]} 35. Rg1 {[%clk 0:00:01.9]} 35... Bc5 {[%clk 0:00:20.5]} 36. h4 {[%clk 0:00:01.9]} 36... Bxg1 {[%clk 0:00:19.9]} 37. hxg5 {[%clk 0:00:01.9]} 37... Kxg5 {[%clk 0:00:20.8]} 0-1', 'time_control': '60+1', 'end_time': 1609687830, 'rated': True, 'fen': '8/6pp/p3p3/1p4k1/8/PP6/2r5/6bK w - -',
# 'time_class': 'bullet', 
# 'rules': 'chess', 
# 'white': {'rating': 1204, 'result': 'timeout', '@id': 'https://api.chess.com/pub/player/adrianojreis', 'username': 'AdrianoJReis'}, 
# 'black': {'rating': 1155, 'result': 'win', '@id': 'https://api.chess.com/pub/player/funvengeance', 'username': 'funvengeance'}}

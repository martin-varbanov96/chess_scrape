from django.db import models

class ChessPlayer(models.Model):
    id = models.AutoField(primary_key=True,)
    username = models.CharField(max_length=200,
                                null=True,
                                unique=True,)

class ChessGame(models.Model):
    id = models.AutoField(primary_key=True,)
    url = models.CharField(max_length=50,
                           null=True,
                           blank=True,
                           unique=True,)

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
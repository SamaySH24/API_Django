# your_app/models.py
from django.db import models

class Player(models.Model):
    player_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    current_price = models.FloatField(null=True, blank=True)
    total_points = models.FloatField(null=True, blank=True)
    cricsheet_key = models.CharField(max_length=50, unique=True, null=True, blank=True)
    key_api = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.player_id} - {self.cricsheet_key}'

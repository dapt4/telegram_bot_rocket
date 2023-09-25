from django.db import models

# Create your models here.
class Chat(models.Model):
    user_id = models.BigIntegerField(blank=False)
    top = models.IntegerField(blank=False)
    middle = models.IntegerField(blank=False, default=0)
    bottom = models.IntegerField(blank=False)
    index = models.IntegerField(blank=False)
    date = models.IntegerField(blank=False)

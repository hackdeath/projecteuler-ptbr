from django.db import models

class Question(models.Model):
    number      = models.PositiveSmallIntegerField()
    name        = models.TextField()
    enunciation = models.TextField()

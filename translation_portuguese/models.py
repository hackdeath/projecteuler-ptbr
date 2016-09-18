from django.db import models

class Question(models.Model):
    number      = models.PositiveSmallIntegerField()
    name        = models.TextField()
    enunciation = models.TextField()
    solved_by   = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return "{0} - {1}".format(self.number, self.name)

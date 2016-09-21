from django.db import models

class Question(models.Model):
    number      = models.PositiveSmallIntegerField()
    name        = models.TextField()
    enunciation = models.TextField()
    solved_by   = models.PositiveSmallIntegerField(default = 0)
    difficulty  = models.PositiveSmallIntegerField(default = 0)
    translated  = models.BooleanField(default = False)

    def __str__(self):
        if (self.translated):
            status = "Tradução concluída"
        else:
            status = "Esperando tradução"

        return "{0} - {1} ({2})".format(self.number, self.name, status)

class Translation(models.Model):
    number_question = models.ForeignKey('Question', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    translation = models.TextField()
from djongo import models

class Uitslag(models.Model):
    label = models.CharField(max_length=100)
    time = models.IntegerField(default=1)
    gender = models.IntegerField(default=1)
    dayNumber = models.IntegerField(default=1)
    temperature = models.IntegerField(default=1)
    regioCode = models.IntegerField(default=1)

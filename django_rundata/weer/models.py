from djongo import models

class Weer(models.Model):
    YYYYMMDD = models.IntegerField(default=1)

class WeerAnalyse(models.Model):
    slope = models.FloatField(default=0),
    intercept = models.FloatField(default=0),
    rvalue = models.FloatField(default=0),
    pvalue = models.FloatField(default=0)

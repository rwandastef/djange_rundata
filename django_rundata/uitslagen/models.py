from djongo import models

class Uitslag(models.Model):
    label = models.CharField(max_length=100)
    time = models.IntegerField(default=1)
    gender = models.IntegerField(default=1)
    dayNumber = models.IntegerField(default=1)
    temperature = models.IntegerField(default=1)
    regioCode = models.IntegerField(default=1)

class AnalysedUitslagen:
   def __init__(self, mean_runtime, slope, intercept, pvalue, rvalue,
                mean_runtime_men, mean_runtime_women):
       self.mean_runtime = mean_runtime
       self.slope = slope
       self.intercept = intercept
       self.pvalue = pvalue
       self.rvalue = rvalue
       self.mean_runtime_men = mean_runtime_men
       self.mean_runtime_women = mean_runtime_women




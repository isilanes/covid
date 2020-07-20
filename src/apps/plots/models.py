from django.db import models


class Country(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Datum(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateTimeField("Date")
    cases = models.IntegerField("Cases", default=0)
    deaths = models.IntegerField("Deaths", default=0)
    recoveries = models.IntegerField("Recoveries", default=0)

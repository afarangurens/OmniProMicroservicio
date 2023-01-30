from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, default="")
    code = models.CharField(max_length=2, default="")

    def __str__(self):
        return "%s" % (self.name)

class Country(models.Model):
    name = models.CharField(max_length=50, default="")
    code = models.CharField(max_length=2, default="")

    def __str__(self):
        return "%s" % (self.name)

class State(models.Model):
    name = models.CharField(max_length=50, default="")
    code = models.CharField(max_length=2, default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

class City(models.Model):
    name = models.CharField(max_length=50, default="")
    code = models.CharField(max_length=2, default="")
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

class Client(models.Model):
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    favorite_stor = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

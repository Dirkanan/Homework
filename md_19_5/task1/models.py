from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    balance = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length = 100)
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    size= models.DecimalField(max_digits=19, decimal_places=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Dish(models.Model):
    dish_name = models.CharField(max_length=40)
    description = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_name
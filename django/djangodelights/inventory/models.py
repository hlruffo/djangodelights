from django.db import models


# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.DecimalField(decimal_places=2, max_digits=5)
    unit = models.CharField(max_length=3)
    ingredient_price = models.DecimalField(decimal_places=2, max_digits=3)


class MenuItem(models.Model):
    title = models.CharField(
        max_length=30, help_text="Enter Menu's Item Name")
    item_price = models.DecimalField(decimal_places=2, max_digits=3)


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=5)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

from django.contrib import admin

from .models import Ingredients, MenuItem, Purchase, RecipeRequirements

# Register your models here.

admin.site.register(Ingredients)
admin.site.register(MenuItem)
admin.site.register(Purchase)
admin.site.register(RecipeRequirements)

from django.contrib import admin
from .models import Pizza, Topping, Tag, IngredientInfo
# Register your models here.

admin.site.register(Topping)
admin.site.register(IngredientInfo)
admin.site.register(Tag)


class IngredientInLine(admin.TabularInline):
    model = IngredientInfo
    extra = 4


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    inlines = [IngredientInLine]
    prepopulated_fields = {
        'slug': ('name',)
    }
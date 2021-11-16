from django.conf import settings
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Pizza(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='ЧПУ', blank=True, unique=True, null=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def get_topping(self):
        return self.ingredientinfo_set.all()

    def get_topping_id(self):
        ids = [ingr.topping.id for ingr in self.ingredientinfo_set.all()]
        return ids

    def add_topping(self, topping, count, measure):
        topping_inst = Topping.objects.get(pk=topping)
        ingredient = IngredientInfo(pizza=self, topping=topping_inst, count=count, measure=measure)
        ingredient.save()

    def get_absolute_url(self):
        return f'/pizza/{self.slug}/'


class Topping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    relation = models.ManyToManyField(Pizza, through='IngredientInfo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class IngredientInfo(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    count = models.FloatField()
    measure = models.CharField(max_length=30, default="грамм")

    def __str__(self):
        return self.topping.name

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Состав'




from django.db import models
from garpix_page.models import BasePage

CHOICES = (
    ("ГОСТИНИЦА", "Гостиница"),
    ("МОТЕЛЬ", "Мотель"),
    ("АПАРТАМЕНТЫ", "Апартаменты"),
)

class Comfort(models.Model):
    title = models.CharField(max_length=255, verbose_name='Удобства')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, default='')

    class Meta:
        verbose_name = 'Удосбтво'
        verbose_name_plural = 'Удобства'

    def __str__(self):
        return self.title



class OneHotelPage(BasePage):
    # name = models.CharField(max_length=255, verbose_name='Название отеля')
    type = models.CharField(max_length=255, verbose_name='Тип отеля', choices=CHOICES)
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, default='')
    comfort = models.ManyToManyField(Comfort, blank=True, verbose_name='Удобства')
    stars = models.PositiveIntegerField(verbose_name='Звезды', blank=True)
    rating = models.FloatField(verbose_name='Рейтинг', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Фото', blank=True)

    template = "pages/one_hotel.html"

    class Meta:
        verbose_name = "Подробно Отель"
        verbose_name_plural = "Подробно Отели"
        ordering = ("-created_at",)

    def get_comfort_title(self):
        return set([x.title for x in self.comfort.all()])

    def get_comfort_id(self):
        return set([x.id for x in self.comfort.all()])
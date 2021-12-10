from django.db import models


class Booking(models.Model):
    date_in = models.DateTimeField(verbose_name='Въезд')
    date_out = models.DateTimeField(verbose_name='Выезд')
    adults = models.IntegerField()
    kids = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
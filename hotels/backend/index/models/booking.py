from django.db import models


class Booking(models.Model):
    date_in = models.CharField(verbose_name='Въезд', max_length=255, )
    date_out = models.CharField(verbose_name='Выезд', max_length=255)
    adults_count = models.PositiveIntegerField(verbose_name='Количество взрослых')
    kids_count = models.PositiveIntegerField(verbose_name='Количество детей')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

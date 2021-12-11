from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from garpix_notify.models import Notify
from garpix_page.models import BasePage

from .booking import Booking
from ..forms.booking import BookingForm


class Navigate(models.Model):
    content = models.CharField(max_length=100, verbose_name='Название ссылки')
    sort = models.IntegerField(default=100, verbose_name='Сортировка',
                               help_text='Чем меньше число, тем выше будет элемент в списке.')

    class Meta:
        verbose_name = 'Название ссылки'
        verbose_name_plural = 'Названия ссылок'
        ordering = ('sort',)


class MainBanner(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название баннера')
    # description = models.CharField(max_length=255, verbose_name='Описание')
    description = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')

    class Meta:
        verbose_name = 'Абзац'
        verbose_name_plural = 'Абзацы'

    def __str__(self):
        return self.title


class Recommendation(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название рекомендации')
    # description = models.CharField(max_length=255, verbose_name='описание')
    description = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'


class Reason(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название причины')
    number = models.PositiveIntegerField()
    description = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    # description = models.CharField(max_length=255, verbose_name='Описание причины')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'

class IndexPage(BasePage):
    main_banner = models.ManyToManyField(MainBanner, blank=True, verbose_name='Абзацы')
    reason = models.ManyToManyField(Reason,  blank=True, verbose_name='Причины')
    recommendation = models.ManyToManyField(Recommendation, blank=True, verbose_name='Рекомендации')

    template = "index.html"

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save()
                Notify.send(settings.BOOKING_EVENT, {"booking": booking})
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })

        return context

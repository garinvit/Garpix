from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class MainBanner(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название баннера')
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title


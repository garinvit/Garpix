from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from .reason import Reason


class Recommendation(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название рекомендации')
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, blank=True, verbose_name='Причина')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'
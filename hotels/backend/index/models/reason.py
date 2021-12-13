from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from .index_page import IndexPage


class Reason(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название причины')
    number = models.PositiveIntegerField(verbose_name='Номер')
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    index_page = models.ForeignKey(IndexPage, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'

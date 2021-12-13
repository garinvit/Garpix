# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# from django.db import models
# from .hotels_page import HotelsPage
#
#
# class SocialLink(models.Model):
#     title = models.CharField(max_length=150, verbose_name='Название кнопки')
#     link = models.URLField(max_length=100, verbose_name='Ссылка')
#     image_svg = RichTextUploadingField(verbose_name='Иконка', blank=True, help_text='Добавьте иконку в формате SVG текстом') # не работает
#     index = models.ForeignKey(HotelsPage, on_delete=models.CASCADE, blank=True)
#
#     class Meta:
#         verbose_name = 'Ссылка на соц.сети'
#         verbose_name_plural = 'Ссылки на соц.сети'
#
#     def __str__(self):
#         return self.title
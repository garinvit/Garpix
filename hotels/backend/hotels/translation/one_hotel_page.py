from modeltranslation.translator import TranslationOptions, register
from ..models import OneHotelPage


@register(OneHotelPage)
class OneHotelPageTranslationOptions(TranslationOptions):
    pass

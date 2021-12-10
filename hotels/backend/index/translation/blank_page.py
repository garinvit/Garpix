from modeltranslation.translator import TranslationOptions, register
from ..models import BlankPage


@register(BlankPage)
class BlankPageTranslationOptions(TranslationOptions):
    pass

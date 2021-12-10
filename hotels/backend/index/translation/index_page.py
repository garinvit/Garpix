from modeltranslation.translator import TranslationOptions, register
from ..models import IndexPage


@register(IndexPage)
class IndexPageTranslationOptions(TranslationOptions):
    pass

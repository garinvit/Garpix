# from ..models.footer import SocialLink
from ..models.hotels_page import HotelsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin

#
# class SocialLinkInLine(admin.TabularInline):
#     model = SocialLink


@admin.register(HotelsPage)
class HotelsPageAdmin(BasePageAdmin):
    # inlines = [SocialLinkInLine]
    pass

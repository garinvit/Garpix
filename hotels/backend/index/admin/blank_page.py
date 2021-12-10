from ..models.blank_page import BlankPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BlankPage)
class BlankPageAdmin(BasePageAdmin):
    pass

from ..models.one_hotel_page import OneHotelPage, Comfort, Type
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


admin.site.register(Comfort)
admin.site.register(Type)


@admin.register(OneHotelPage)
class OneHotelPageAdmin(BasePageAdmin):
    pass


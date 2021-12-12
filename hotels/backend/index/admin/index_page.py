from ..models.index_page import IndexPage, Reason, Recommendation, MainBanner
from ..models.booking import Booking
from django.contrib import admin
from garpix_page.admin import BasePageAdmin

class MainBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')


class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number', 'content')


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date_in', 'date_out', 'adults', 'kids')
    readonly_fields = ('created_at',)

admin.site.register(Reason, ReasonAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(MainBanner, MainBannerAdmin)


# class ReasonInLine(admin.TabularInline):
#     model = Reason
#
#
# class BannerInLine(admin.TabularInline):
#     model = MainBanner
#
#
# class RecommendationInLine(admin.TabularInline):
#     model = Recommendation
#

# @admin.register(IndexPage)
# class IndexPageAdmin(BasePageAdmin):
#     inlines = [ReasonInLine, BannerInLine, RecommendationInLine]

@admin.register(IndexPage)
class IndexPageAdmin(BasePageAdmin):
    pass
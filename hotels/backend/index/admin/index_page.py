from ..models.index_page import IndexPage
from ..models.reason import Reason
from ..models.recommendation import Recommendation
from ..models.banner import MainBanner
from ..models.booking import Booking
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(MainBanner)
class MainBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date_in', 'date_out', 'adults_count', 'kids_count')
    readonly_fields = ('created_at',)


class RecommendationInLine(admin.TabularInline):
    model = Recommendation
    extra = 3


class ReasonInLine(admin.TabularInline):
    model = Reason


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number', 'content')
    inlines = [RecommendationInLine]


@admin.register(IndexPage)
class IndexPageAdmin(BasePageAdmin):
    inlines = [ReasonInLine]


admin.site.register(Recommendation)

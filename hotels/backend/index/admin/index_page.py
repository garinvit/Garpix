from ..models.index_page import IndexPage, Reason, Recommendation, MainBanner
from django.contrib import admin
from garpix_page.admin import BasePageAdmin

class MainBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number', 'description')


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


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
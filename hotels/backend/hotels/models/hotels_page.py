from django.db import models
from garpix_page.models import BaseListPage


class HotelsPage(BaseListPage):
    paginate_by = 3
    template = 'hotels.html'

    class Meta:
        verbose_name = "Отели"
        verbose_name_plural = "Отели"
        ordering = ('-created_at',)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        print(context)
        print(request.GET)
        return context
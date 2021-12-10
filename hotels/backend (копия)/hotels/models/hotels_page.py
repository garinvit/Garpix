from django.db import models
from garpix_page.models import BasePage


class HotelsPage(BasePage):
    template = "hotels.html"

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        ordering = ("-created_at",)

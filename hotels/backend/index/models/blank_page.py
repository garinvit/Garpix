from django.db import models
from garpix_page.models import BasePage


class BlankPage(BasePage):
    template = "blank.html"

    class Meta:
        verbose_name = "Blank"
        verbose_name_plural = "Blanks"
        ordering = ("-created_at",)

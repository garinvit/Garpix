from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from garpix_notify.models import Notify
from garpix_page.models import BasePage

from .banner import MainBanner
from .booking import Booking
from ..forms.booking import BookingForm


class IndexPage(BasePage):
    top_banner = models.ForeignKey(MainBanner, on_delete=models.CASCADE, blank=True, verbose_name='Верхний баннер',
                                   related_name="top_banner")
    middle_banner = models.ForeignKey(MainBanner, on_delete=models.CASCADE, blank=True, verbose_name='Средний баннер',
                                      related_name="middle_banner")
    bottom_banner = models.ForeignKey(MainBanner, on_delete=models.CASCADE, blank=True, verbose_name='Нижний баннер',
                                      related_name="bottom_banner")
    template = "index.html"

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save()
                Notify.send(settings.BOOKING_EVENT, {"booking": booking})
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })

        return context


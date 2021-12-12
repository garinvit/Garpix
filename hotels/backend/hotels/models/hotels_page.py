from django.db import models
from garpix_page.models import BaseListPage
from garpix_utils.paginator import GarpixPaginator
from .one_hotel_page import Comfort, OneHotelPage, CHOICES

class HotelsPage(BaseListPage):
    paginate_by = 3
    template = 'hotels.html'

    class Meta:
        verbose_name = "Отели"
        verbose_name_plural = "Отели"
        ordering = ('-created_at',)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        types = [x[1] for x in CHOICES]
        context.update({"comfort": Comfort.objects.all(), "types": types})

        if request.GET:
            request_set = set(request.GET.dict())
            comfort_set = set([x.title for x in Comfort.objects.all()]).intersection(request_set)
            types_set = [x.upper() for x in set(types).intersection(request_set)]
            # print("comfort set", comfort_set, types_set, request_set)
            object_list = OneHotelPage.objects.filter(type__in=types_set)
            object_list = [x for x in object_list if comfort_set.issubset(x.get_comfort_title())]
            paginator = GarpixPaginator(object_list, self.paginate_by)
            try:
                page = int(request.GET.get('page', 1))
            except ValueError:
                page = 1

            paginated_object_list = paginator.get_page(page)

            context.update({
                'paginator': paginator,
                'paginated_object_list': paginated_object_list,
                'page': page,
                'obj_len': len(object_list),
            })
        return context
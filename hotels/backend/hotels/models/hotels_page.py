from django.db import models
from django.db.models import Max
from garpix_page.models import BaseListPage
from garpix_utils.paginator import GarpixPaginator
from .one_hotel_page import Comfort, OneHotelPage, Type


class HotelsPage(BaseListPage):
    paginate_by = 3
    template = 'hotels.html'

    class Meta:
        verbose_name = "Отели"
        verbose_name_plural = "Отели"
        ordering = ('-created_at',)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        types = Type.objects.all()
        hotels = OneHotelPage.objects.all()
        comforts = Comfort.objects.all()
        context.update({"comfort": comforts,
                        "types": types,
                        'obj_len': len(hotels),
                        'max_price': hotels.aggregate(Max('price')).get('price__max'),
                        })
        if request.GET:
            request_set = set(request.GET.dict())
            object_list = hotels
            try:
                min_price = int(request.GET.get('min-price'))
            except (ValueError, TypeError):
                min_price = 0
            try:
                max_price = int(request.GET.get('max-price'))
            except (ValueError, TypeError):
                max_price = 0
            comfort_set = set([x.title for x in comforts]).intersection(request_set)
            types_set = set([x.title for x in types]).intersection(request_set)
            if types_set:
                object_list = hotels.filter(type__title__in=types_set)
            if min_price:
                object_list = object_list.filter(price__gte=min_price)
            if max_price:
                object_list = object_list.filter(price__lte=max_price)
            # if comfort_set:  # or filter
            #     object_list = object_list.filter(comfort__title__in=comfort_set).distinct()
            if comfort_set:  # and filter
                for i in comfort_set:
                    object_list = object_list.filter(comfort__title=i).distinct()
            ordering = request.GET.get('ordering')
            if ordering:
                if ordering[0] == '+':
                    object_list = object_list.order_by(ordering[1:])
                else:
                    object_list = object_list.order_by(ordering)

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

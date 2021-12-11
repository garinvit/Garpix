from garpixcms.settings import *  # noqa


INSTALLED_APPS += [
    'index',
    'hotels',
]

MENU_TYPE_HEADER_MENU = 'header_menu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
    },
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]

BOOKING_EVENT = 1

NOTIFY_EVENTS = {
    BOOKING_EVENT: {
        'title': 'Бронирование',
    },
}
CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

# CHOICES_NOTIFY_EVENT = sorted([(k, v['title']) for k, v in NOTIFY_EVENTS.items()], key=lambda x: x[1])
from garpixcms.settings import *  # noqa


INSTALLED_APPS += [
    'index',
    'hotels',
]

MENU_TYPE_HEADER_MENU = 'header_menu'
MENU_TYPE_FOOTER_MENU = 'footer_menu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Оглавление',
    },
    MENU_TYPE_FOOTER_MENU: {
        'title': 'Соц.сети',
    },
}

BOOKING_EVENT = 1

NOTIFY_EVENTS = {
    BOOKING_EVENT: {
        'title': 'Бронирование',
    },
}
CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

# CHOICES_NOTIFY_EVENT = sorted([(k, v['title']) for k, v in NOTIFY_EVENTS.items()], key=lambda x: x[1])
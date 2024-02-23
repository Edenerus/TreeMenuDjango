from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import TreeMenuItem


register = template.Library()




@register.inclusion_tag('menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):
    items = TreeMenuItem.objects.filter(menu__name=menu_name)

    def get_menu(menu_item: str = None, submenu: list = None):

        menu = list(items.filter(parent=None)) if menu_item is None \
            else list(items.filter(parent__name=menu_item))

        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass

        try:
            return get_menu(menu_item=items.get(name=menu_item).parent.name, submenu=menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    return {'menu': get_menu()} if menu_name == menu_item \
        else {'menu': get_menu(menu_item)}

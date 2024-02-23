from django.shortcuts import render

from .models import TreeMenu


def index(request):
    return render(request, 'main.html', {'menus': TreeMenu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0
    print(splitted_path)
    return render(request, 'main.html', context={'menu_name': splitted_path[0],
                                                 'menu_item': splitted_path[-1]})

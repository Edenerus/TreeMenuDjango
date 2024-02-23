from django.contrib import admin
from .models import TreeMenu, TreeMenuItem


@admin.register(TreeMenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(TreeMenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'menu', )
    list_filter = ('menu', )

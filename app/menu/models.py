from django.db import models


class InfoMixin(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")

    class Meta:
        abstract = True


class TreeMenu(InfoMixin):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class TreeMenuItem(InfoMixin):
    menu = models.ForeignKey(TreeMenu, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родитель')
    url = models.CharField(
        verbose_name='URL-адрес',
        max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

from django.contrib import admin
from .models import Category, Goods, Product, Client, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name_of_product', 'quantity']
    ordering = ['name_of_product', '-quantity']
    list_filter = ['date_of_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт"""
    fields = ['name_of_product', 'description', 'date_of_add']
    readonly_fields = ['date_of_add']
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             'classes': ['wide'],
    #             'fields': ['name_of_product'],
    #         },
    #     ),
    #     (
    #         'Подробности',
    #         {
    #             'classes': ['collapse'],
    #             'description': 'Категория товара и его подробое описание',
    #             'fields': ['description'],
    #         },
    #     ),
    #     (
    #         'Бухгалтерия',
    #         {
    #             'fields': ['price', 'quantity'],
    #         }
    #     ),
    # ]

class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['name', 'email', 'phone_number', 'address']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя клиента'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Goods)

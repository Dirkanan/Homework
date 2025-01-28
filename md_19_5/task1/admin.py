from django.contrib import admin
from .models import Game, Buyer, News


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Настройка полей для поиска
    search_fields = ['title']

    # Фильтрация по полям
    list_filter = ['size', 'cost']

    # Поля, отображаемые в списке
    list_display = ['title', 'cost', 'size']

    # Ограничение количества записей
    list_per_page = 20

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['title', 'date']
    list_display = ['title', 'content', 'date']
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Настройка полей для поиска
    search_fields = ['name']

    # Фильтрация по полям
    list_filter = ['balance', 'age']

    # Поля, отображаемые в списке
    list_display = ['name', 'balance', 'age']

    # Ограничение количества записей
    list_per_page = 30

    # Устанавливаем поле balance как доступное только для чтения
    def get_readonly_fields(self, request, obj=None):
        return ['balance'] if obj else []

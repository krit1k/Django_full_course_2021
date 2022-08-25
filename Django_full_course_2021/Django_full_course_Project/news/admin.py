from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):

    '''
    Класс-редактор (News)
    '''

    # передаём те поля которые хотим видеть в админке (в приложении news/НОВОСТИ)
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    # передаём те поля которые должны быть ссылками на объект модели News
    list_display_links = ('id', 'title')
    # передаём поля по которым можно производить поиск объектов в админке
    search_fields = ('title', 'content')
    # указываем поля, которые хотим редактировать из списка всех объектов таблицы (в админке)
    list_editable = ('is_published',)
    # указываем поля по которым можно будет отфильтровать новости (окошко ФИЛЬТР справа от списка)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):

    '''
    Класс-редактор (Category)
    '''

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin) # первым регистрируется основная модель, а потом модель настраивающая её
admin.site.register(Category, CategoryAdmin)

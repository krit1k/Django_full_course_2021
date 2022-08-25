from django.db import models

class News(models.Model):

    '''
    Таблица новостей (вторичная по отношению к Category)
    '''

    title = models.CharField(max_length=120)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    # организуем связь с таблицей Category
    # в таблице к category будет добавлено _id из-за ForeignKey
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:

        '''
        Мета класс
        '''

        verbose_name = 'Новость' # то, как будет именоваться модель в ед.числе
        verbose_name_plural = 'Новости' # аналогично для мн.числа
        ordering = ['-created_at'] # как будут сортироваться экземпляры модели (можно передать несколько критериев)


    def __str__(self):
        return self.title


class Category(models.Model):

    '''
    Таблица категорий (первичная по отношению к News)
    '''

    title = models.CharField(max_length=60, db_index=True)


    class Meta:

        '''
        Мета класс
        '''

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

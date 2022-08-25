from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    verbose_name = 'Новости' # то, как будет именоваться приложение news в админке

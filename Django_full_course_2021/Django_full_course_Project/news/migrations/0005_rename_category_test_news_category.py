# Generated by Django 4.1 on 2022-08-25 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_category_news_category_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='category_test',
            new_name='category',
        ),
    ]
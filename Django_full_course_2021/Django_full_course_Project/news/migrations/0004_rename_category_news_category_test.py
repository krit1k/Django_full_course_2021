# Generated by Django 4.1 on 2022-08-25 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_news_photo_alter_news_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='category',
            new_name='category_test',
        ),
    ]

# Generated by Django 3.1 on 2021-12-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20211210_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='Название ссылки')),
                ('sort', models.IntegerField(default=100, help_text='Чем меньше число, тем выше будет элемент в списке.', verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'Название ссылки',
                'verbose_name_plural': 'Названия ссылок',
                'ordering': ('sort',),
            },
        ),
    ]

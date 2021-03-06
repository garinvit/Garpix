# Generated by Django 3.1 on 2021-12-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_blankpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateTimeField(verbose_name='Въезд')),
                ('date_out', models.DateTimeField(verbose_name='Выезд')),
                ('adults', models.PositiveIntegerField()),
                ('kids', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
                'ordering': ('-created_at',),
            },
        ),
    ]

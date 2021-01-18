# Generated by Django 3.0.11 on 2021-01-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возвраст')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возвраст')),
                ('licence_id', models.IntegerField(verbose_name='ID лицензии')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), verbose_name='Рейтинг')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
            ],
        ),
    ]
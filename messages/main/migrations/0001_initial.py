# Generated by Django 2.2.19 on 2023-01-17 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Город')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Список доноров')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='InterviewTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('cities', models.ManyToManyField(help_text='Выберите время собеседования', to='main.City', verbose_name='Время собеседования')),
            ],
            options={
                'verbose_name': 'Время собеседования',
                'verbose_name_plural': 'Время собеседований',
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=250, null=True, verbose_name='Город')),
                ('vacancy', models.TextField(blank=True, max_length=250, null=True, verbose_name='Список вакансий')),
            ],
            options={
                'verbose_name': 'Приоритет',
                'verbose_name_plural': 'Приоритеты',
            },
        ),
        migrations.CreateModel(
            name='SampleResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=300, null=True)),
                ('number', models.CharField(help_text='Вставьте номер кандидата', max_length=20, verbose_name='Номер кандидата')),
            ],
            options={
                'verbose_name': 'Шаблон отклика',
                'verbose_name_plural': 'Шаблоны отклика',
            },
        ),
        migrations.CreateModel(
            name='SampleStraight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(blank=True, help_text='Введите своё имя', max_length=30, null=True, verbose_name='Имя')),
                ('number', models.CharField(help_text='Вставьте номер кандидата', max_length=20, verbose_name='Номер кандидата')),
            ],
            options={
                'verbose_name': 'Шаблон прямого поиска',
                'verbose_name_plural': 'Шаблоны прямых поисков',
            },
        ),
        migrations.CreateModel(
            name='Zapros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer', models.TextField(blank=True, max_length=500, null=True, verbose_name='Пример шапки запроса')),
                ('city', models.TextField(max_length=500, verbose_name='Площадка')),
                ('title', models.TextField(blank=True, max_length=500, null=True, verbose_name='Шапка сообщения')),
                ('town', models.CharField(blank=True, help_text='Введите город', max_length=100, null=True, verbose_name='Город')),
                ('name', models.CharField(blank=True, help_text='Введите ФИО', max_length=100, null=True, verbose_name='ФИО')),
                ('number', models.CharField(blank=True, help_text='Введите номер телефона', max_length=20, null=True, verbose_name='Номер телефона')),
                ('baza', models.TextField(blank=True, help_text='Вставьте ссылку на анкету', null=True, verbose_name='Ссылка на анкету')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Заголовок')),
                ('weektime', models.DateField(blank=True, help_text='Выберите дату собеседования', null=True, verbose_name='Дата собеседования')),
                ('text', models.TextField(help_text='Введите текст сообщения', verbose_name='Текст сообщения')),
                ('number', models.CharField(blank=True, help_text='Вставьте номер кандидата', max_length=20, null=True, verbose_name='Номер кандидата')),
                ('cities', models.ForeignKey(blank=True, help_text='Выберите город', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.City', verbose_name='Город')),
                ('hourtime', models.ForeignKey(blank=True, help_text='Выберите время собеседования', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.InterviewTime', verbose_name='Время собеседования')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]

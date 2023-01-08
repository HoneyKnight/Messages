from django.db import models


class Message(models.Model):
    title = models.TextField(
        null=True,
        blank=True,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст сообщения',
        help_text='Введите текст сообщения',
    )
    weektime = models.DateField(
        verbose_name='Дата собеседования',
        help_text='Выберите дату собеседования',
        blank=True,
        null=True
    )
    hourtime = models.ForeignKey(
        'SobesTime',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Время собеседования',
        help_text='Выберите время собеседования'
    )
    cities = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Выберите город',
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text[:15]


class City(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        verbose_name='Город'
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Список доноров'
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class SobesTime(models.Model):
    value = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = 'Время собеседования'
        verbose_name_plural = 'Время собеседований'

    def __str__(self):
        return self.value


class Prioritet(models.Model):
    city = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Город'
    )
    vacancy = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Список вакансий'
    )

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return self.city


class Zapros(models.Model):
    primer = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Пример шапки запроса'
    )
    city = models.TextField(
        max_length=500,
        verbose_name='Площадка'
    )
    title = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Шапка сообщения'
    )
    town = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Введите город'
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='ФИО',
        help_text='Введите ФИО'
    )
    number = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона'
    )
    baza = models.TextField(
        blank=True,
        null=True,
        verbose_name='Ссылка на анкету',
        help_text='Вставьте ссылку на анкету'
    )

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return 'Запрос'

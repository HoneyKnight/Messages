from django.db import models


class Message(models.Model):
    title = models.TextField(
        null=True,
        blank=True,
        verbose_name='Заголовок'
    )
    weektime = models.DateField(
        verbose_name='Дата собеседования',
        help_text='Выберите дату собеседования',
        blank=True,
        null=True
    )
    hourtime = models.ForeignKey(
        'InterviewTime',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Время собеседования',
        help_text='Выберите время собеседования'
    )
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст сообщения',
        help_text='Введите текст сообщения',
    )
    cities = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Выберите город',
    )
    number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Номер кандидата',
        help_text='Вставьте номер кандидата'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text


class MessageOffice(models.Model):
    title = models.TextField(
        null=True,
        blank=True,
        verbose_name='Заголовок'
    )
    weektime = models.DateField(
        verbose_name='Дата собеседования',
        help_text='Выберите дату собеседования',
        blank=True,
        null=True
    )
    hourtime = models.ForeignKey(
        'InterviewTimeOffice',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Время собеседования',
        help_text='Выберите время собеседования'
    )
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст сообщения',
        help_text='Введите текст сообщения',
    )
    cities = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Выберите город',
    )
    number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Номер кандидата',
        help_text='Вставьте номер кандидата'
    )

    class Meta:
        verbose_name = 'Сообщение_Офис'
        verbose_name_plural = 'Сообщения_Офис'

    def __str__(self):
        return self.text


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


class InterviewTime(models.Model):
    value = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = 'Время собеседования'
        verbose_name_plural = 'Время собеседований'
        ordering = ['value']

    def __str__(self):
        return self.value


class InterviewTimeOffice(models.Model):
    value = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = 'Время собеседования в офисе'
        verbose_name_plural = 'Время собеседований в офисе'

    def __str__(self):
        return self.value


class Priority(models.Model):
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
    number = models.CharField(
        max_length=20,
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


class SampleResponse(models.Model):
    text = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер кандидата',
        help_text='Вставьте номер кандидата'
    )

    class Meta:
        verbose_name = 'Шаблон отклика'
        verbose_name_plural = 'Шаблоны отклика'

    def __str__(self):
        return 'Шаблон отклика'


class SampleStraight(models.Model):
    text = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Имя',
        help_text='Введите своё имя'
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер кандидата',
        help_text='Вставьте номер кандидата'
    )

    class Meta:
        verbose_name = 'Шаблон прямого поиска'
        verbose_name_plural = 'Шаблоны прямых поисков'

    def __str__(self):
        return 'Шаблон прямого поиска'

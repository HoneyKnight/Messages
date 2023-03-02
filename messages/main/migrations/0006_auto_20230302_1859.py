# Generated by Django 3.2.16 on 2023-03-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230224_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zapros',
            name='title',
        ),
        migrations.AddField(
            model_name='zapros',
            name='text',
            field=models.TextField(default=1, help_text='Введите текст сообщения', max_length=300, verbose_name='Текст сообщения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zapros',
            name='number',
            field=models.CharField(default=1, help_text='Вставьте номер кандидата', max_length=20, verbose_name='Номер кандидата'),
            preserve_default=False,
        ),
    ]
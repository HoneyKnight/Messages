# Generated by Django 3.2.16 on 2023-03-10 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230302_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='cities',
            field=models.ForeignKey(blank=True, help_text='Выберите город', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='main.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='message',
            name='hourtime',
            field=models.ForeignKey(blank=True, help_text='Выберите время собеседования', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='main.interviewtime', verbose_name='Время собеседования'),
        ),
    ]
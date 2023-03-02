# Generated by Django 3.2.16 on 2023-02-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230222_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplestraight',
            name='sampleresponse_ptr',
        ),
        migrations.AddField(
            model_name='samplestraight',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='samplestraight',
            name='number',
            field=models.CharField(default=1, help_text='Вставьте номер кандидата', max_length=20, verbose_name='Номер кандидата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='samplestraight',
            name='text',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
# Generated by Django 3.2.16 on 2023-02-22 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230118_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplestraight',
            name='id',
        ),
        migrations.RemoveField(
            model_name='samplestraight',
            name='number',
        ),
        migrations.RemoveField(
            model_name='samplestraight',
            name='text',
        ),
        migrations.AddField(
            model_name='samplestraight',
            name='sampleresponse_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.sampleresponse'),
            preserve_default=False,
        ),
    ]
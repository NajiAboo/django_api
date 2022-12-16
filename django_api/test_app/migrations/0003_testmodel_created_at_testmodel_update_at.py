# Generated by Django 4.1.4 on 2022-12-16 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_rename_is_live_testmodel_is_alive'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='update_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-16 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='is_live',
            new_name='is_Alive',
        ),
    ]

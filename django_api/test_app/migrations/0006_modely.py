# Generated by Django 4.1.4 on 2022-12-16 08:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_testmodel_options_modelx'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateField(default=django.utils.timezone.now)),
                ('test_content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test_content_y', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelY',
                'ordering': ('-created_at',),
            },
        ),
    ]
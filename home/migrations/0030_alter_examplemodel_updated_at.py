# Generated by Django 4.2.14 on 2024-11-28 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_examplemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
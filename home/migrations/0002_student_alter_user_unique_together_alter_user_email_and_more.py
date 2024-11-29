# Generated by Django 4.1.12 on 2023-12-08 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.BigIntegerField(error_messages={'unique': 'A user with that Student ID already exists.'}, help_text='Required. Enter Deakin Student ID. Digits only.', primary_key=True, serialize=False, unique=True, validators=[home.validators.StudentIdValidator], verbose_name='student_id')),
                ('allocated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='allocated', to='home.project')),
                ('p1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p1', to='home.project')),
                ('p2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p2', to='home.project')),
                ('p3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p3', to='home.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='deakin email address'),
        ),
        migrations.DeleteModel(
            name='ProjectPriority',
        ),
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
    ]

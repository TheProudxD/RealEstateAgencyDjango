# Generated by Django 5.1.2 on 2024-11-16 15:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0008_alter_agent_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='photo',
            field=models.ImageField(default="", upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
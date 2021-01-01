# Generated by Django 3.1.4 on 2020-12-31 09:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studybox', '0002_auto_20201231_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_by',
            field=models.ManyToManyField(blank=True, default=None, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
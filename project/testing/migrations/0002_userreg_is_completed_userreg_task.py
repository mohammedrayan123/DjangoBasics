# Generated by Django 4.2.7 on 2024-02-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userreg',
            name='task',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

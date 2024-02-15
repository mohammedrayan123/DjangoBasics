# Generated by Django 4.2.7 on 2023-12-01 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('taskid', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('taskTitle', models.TextField(max_length=255)),
                ('taskDesc', models.TextField(null=True)),
                ('taskCreated', models.DateTimeField(default=datetime.datetime(2023, 12, 1, 13, 48, 46, 300781))),
                ('taskComp', models.DateTimeField()),
            ],
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-28 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyApp', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 28, 8, 25, 16, 986476, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]

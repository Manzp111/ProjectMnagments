# Generated by Django 5.1.4 on 2024-12-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tenants', 'Tenants'), ('Landroad', 'Landroad')], default='Tenants', max_length=100),
        ),
    ]

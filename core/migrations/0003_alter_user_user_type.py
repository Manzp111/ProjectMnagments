# Generated by Django 5.1.4 on 2024-12-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User'), ('Tenants', 'Tenants'), ('Landlord', 'Landroad')], default='User', max_length=100),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tenants', 'Tenants'), ('Landroad', 'Landroad')], default='Tenants', max_length=100),
        ),
    ]
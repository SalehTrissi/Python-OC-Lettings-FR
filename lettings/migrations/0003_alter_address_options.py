# Generated by Django 5.1.2 on 2024-10-18 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_migrate_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191122_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='total_memory_ram_supported',
            field=models.CharField(choices=[('16GB', 'Até 16 GB'), ('64 GB', 'Até 64 GB')], max_length=10, verbose_name='Total de memórias RAM suportado'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-20 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletePC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Memory_ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory_ram', to='products.MemoryRAM')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motherboard', to='products.Motherboard')),
                ('name_client', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nome do cliente')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processor', to='products.Processor')),
                ('video_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_board', to='products.VideoBoard')),
            ],
            options={
                'verbose_name': 'Computador Completo',
                'verbose_name_plural': 'Computadores Completos',
            },
        ),
    ]

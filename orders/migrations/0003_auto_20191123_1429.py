# Generated by Django 2.2.7 on 2019-11-23 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191123_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completepc',
            name='video_board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_board', to='products.VideoBoard'),
        ),
    ]
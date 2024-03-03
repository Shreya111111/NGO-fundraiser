# Generated by Django 2.2.28 on 2023-06-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0025_auto_20230620_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundraiser',
            name='photo_800',
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='photo_small',
            field=models.ImageField(blank=True, upload_to='photos_small/'),
        ),
    ]

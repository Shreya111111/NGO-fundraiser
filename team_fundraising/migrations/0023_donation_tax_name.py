# Generated by Django 2.2.28 on 2023-02-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0022_auto_20200308_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='tax_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

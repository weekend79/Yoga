# Generated by Django 3.1.1 on 2020-09-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200922_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
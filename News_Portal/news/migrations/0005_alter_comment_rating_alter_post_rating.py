# Generated by Django 5.0.3 on 2024-04-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]

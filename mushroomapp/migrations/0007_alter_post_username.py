# Generated by Django 3.2.23 on 2023-12-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroomapp', '0006_alter_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
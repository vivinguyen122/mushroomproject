# Generated by Django 3.2.23 on 2023-12-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroomapp', '0008_remove_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='anon', max_length=255),
        ),
    ]

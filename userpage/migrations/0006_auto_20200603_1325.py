# Generated by Django 3.0.6 on 2020-06-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0005_auto_20200602_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='user_images/Post'),
        ),
    ]

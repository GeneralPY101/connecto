# Generated by Django 3.0.6 on 2020-06-09 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpage', '0017_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='ref_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referenced_post', to='userpage.Post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='ref_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referenced_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

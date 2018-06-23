# Generated by Django 2.0.6 on 2018-06-22 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180622_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='User_idUser',
        ),
        migrations.AlterField(
            model_name='elections',
            name='User_idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='voting',
            name='User_idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

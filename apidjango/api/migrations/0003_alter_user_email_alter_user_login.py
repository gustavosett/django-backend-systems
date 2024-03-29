# Generated by Django 4.1 on 2022-08-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_login_user_rename_nickname_user_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]

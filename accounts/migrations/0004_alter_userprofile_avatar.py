# Generated by Django 4.0.6 on 2022-07-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_age_remove_userprofile_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatars/user_avatar.png', upload_to='avatars/'),
        ),
    ]
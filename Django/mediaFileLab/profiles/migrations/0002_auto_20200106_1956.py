# Generated by Django 3.0.2 on 2020-01-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_images\\default1.png', upload_to='profile_images'),
        ),
    ]
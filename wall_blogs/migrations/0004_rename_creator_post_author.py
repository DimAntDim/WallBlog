# Generated by Django 3.2.6 on 2021-08-05 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_blogs', '0003_auto_20210805_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creator',
            new_name='author',
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-05 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Profile_name',
            new_name='p_name',
        ),
    ]

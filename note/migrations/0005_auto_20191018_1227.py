# Generated by Django 2.2.3 on 2019-10-18 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_todo_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='index',
            new_name='ind',
        ),
    ]
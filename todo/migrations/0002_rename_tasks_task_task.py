# Generated by Django 4.2.4 on 2023-09-25 18:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="tasks",
            new_name="task",
        ),
    ]
# Generated by Django 5.0.7 on 2024-11-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0003_remove_userprofile_age_rfidcard_uid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="age",
            field=models.IntegerField(null=True),
        ),
    ]

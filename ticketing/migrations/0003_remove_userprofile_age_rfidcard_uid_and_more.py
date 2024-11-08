# Generated by Django 5.0.7 on 2024-11-07 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0002_remove_rfidcard_rfid_number_userprofile_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="age",
        ),
        migrations.AddField(
            model_name="rfidcard",
            name="uid",
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name="RFIDCardLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_latitude", models.DecimalField(decimal_places=9, max_digits=9)),
                (
                    "start_longitude",
                    models.DecimalField(decimal_places=6, max_digits=9),
                ),
                ("end_latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("end_longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "rfid_card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticketing.rfidcard",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

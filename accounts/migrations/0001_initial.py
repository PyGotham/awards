# Generated by Django 3.2.7 on 2021-10-02 00:00

from __future__ import annotations

import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
            "CREATE EXTENSION IF NOT EXISTS citext", reverse_sql=migrations.RunSQL.noop
        ),
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    django.contrib.postgres.fields.citext.CIEmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="password"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False, verbose_name="user can access the admin"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

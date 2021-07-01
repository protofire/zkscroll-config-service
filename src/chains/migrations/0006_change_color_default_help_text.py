# Generated by Django 3.2.4 on 2021-07-01 08:46

import re

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chains", "0005_chain_relevance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="theme_background_color",
            field=models.CharField(
                default="#000000",
                help_text="Please use the following format: <em>#RRGGBB</em>.",
                max_length=9,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^#[0-9a-fA-F]{6}$"), "Invalid hex color", "invalid"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="chain",
            name="theme_text_color",
            field=models.CharField(
                default="#ffffff",
                help_text="Please use the following format: <em>#RRGGBB</em>.",
                max_length=9,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^#[0-9a-fA-F]{6}$"), "Invalid hex color", "invalid"
                    )
                ],
            ),
        ),
    ]

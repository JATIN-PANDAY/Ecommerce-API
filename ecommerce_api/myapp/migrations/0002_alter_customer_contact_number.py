# Generated by Django 5.1.2 on 2024-10-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="contact_number",
            field=models.CharField(max_length=10),
        ),
    ]

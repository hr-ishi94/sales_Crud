# Generated by Django 5.1.2 on 2024-11-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_sales_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]

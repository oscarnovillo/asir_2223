# Generated by Django 4.2.3 on 2023-08-04 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={"permissions": [("can_eat_pizzas", "Can eat pizzas")]},
        ),
    ]
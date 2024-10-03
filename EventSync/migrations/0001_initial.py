# Generated by Django 5.1.1 on 2024-10-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="employees_info",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("Mob_no", models.IntegerField(max_length=20)),
            ],
            options={
                "db_table": "employees_info",
            },
        ),
    ]

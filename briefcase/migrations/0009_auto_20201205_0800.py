# Generated by Django 3.1.3 on 2020-12-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("briefcase", "0008_auto_20201205_0753"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=35),
        ),
    ]

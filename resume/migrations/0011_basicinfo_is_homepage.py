# Generated by Django 3.1.3 on 2021-10-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_basicinfo_cv_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='is_homepage',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.3 on 2021-08-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210510_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='image',
            field=models.CharField(help_text='Use emoji icons https://emojipedia.org/', max_length=8),
        ),
    ]
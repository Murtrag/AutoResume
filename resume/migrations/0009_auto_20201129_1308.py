# Generated by Django 3.1.3 on 2020-11-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20201129_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioncontent',
            name='name',
            field=models.CharField(help_text='this field does not have anny effect on resume it is just a human readable name for an object', max_length=20),
        ),
    ]

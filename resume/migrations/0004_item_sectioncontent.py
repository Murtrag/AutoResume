# Generated by Django 3.1.3 on 2020-11-29 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SectionContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.item')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.section')),
            ],
        ),
    ]

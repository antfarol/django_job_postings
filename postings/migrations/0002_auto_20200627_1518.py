# Generated by Django 3.0.3 on 2020-06-27 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(default='https://place-hold.it/100x60', max_length=200),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.CharField(default='https://place-hold.it/100x60', max_length=200),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
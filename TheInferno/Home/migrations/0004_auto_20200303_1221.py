# Generated by Django 3.0.3 on 2020-03-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_bookclub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookclub',
            name='Amenities',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]

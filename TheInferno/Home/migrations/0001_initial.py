# Generated by Django 3.0.3 on 2020-03-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('DOB', models.DateField(auto_now_add=True)),
                ('pincode', models.IntegerField(max_length=6)),
                ('contact', models.IntegerField(max_length=13)),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bday', models.DateField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]

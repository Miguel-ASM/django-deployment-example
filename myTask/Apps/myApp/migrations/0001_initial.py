# Generated by Django 3.0.3 on 2020-04-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riderName', models.CharField(max_length=60)),
                ('riderBirthData', models.DateField()),
                ('bikeBrand', models.CharField(max_length=60)),
                ('bikeModel', models.CharField(max_length=60)),
            ],
        ),
    ]

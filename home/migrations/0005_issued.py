# Generated by Django 4.1.3 on 2022-11-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20)),
                ('bookname', models.CharField(max_length=40)),
                ('customername', models.CharField(max_length=40)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('charge', models.CharField(max_length=5)),
                ('returned', models.BooleanField()),
            ],
        ),
    ]

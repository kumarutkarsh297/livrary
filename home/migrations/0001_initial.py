# Generated by Django 4.1.3 on 2022-11-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('bisbn', models.CharField(max_length=20)),
                ('bauthor', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]

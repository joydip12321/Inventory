# Generated by Django 4.2.5 on 2023-10-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=50)),
                ('receipe_des', models.TextField()),
                ('receipe_color', models.CharField(max_length=30)),
            ],
        ),
    ]

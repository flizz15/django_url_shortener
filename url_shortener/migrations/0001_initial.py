# Generated by Django 3.0.2 on 2020-05-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('short_link', models.URLField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]

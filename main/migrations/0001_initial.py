# Generated by Django 4.0.5 on 2022-06-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyID', models.CharField(default='', max_length=255)),
                ('username', models.CharField(default='', max_length=255)),
                ('sessionID', models.CharField(default='', max_length=255)),
                ('customerID', models.CharField(default='', max_length=255)),
                ('vendorName', models.CharField(default='', max_length=255)),
                ('vendorImage', models.CharField(default='', max_length=255)),
            ],
        ),
    ]

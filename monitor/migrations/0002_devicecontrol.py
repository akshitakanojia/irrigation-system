# Generated by Django 2.0.3 on 2018-03-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorrequest',
            name='field_of_operation',
            field=models.CharField(default='resdent doctor', max_length=50),
        ),
        migrations.AddField(
            model_name='doctorrequest',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='female', max_length=10),
        ),
    ]

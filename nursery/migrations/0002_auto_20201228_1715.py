# Generated by Django 3.1.4 on 2020-12-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
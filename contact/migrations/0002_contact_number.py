# Generated by Django 2.2.3 on 2019-07-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howmanytimes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='last_collection',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

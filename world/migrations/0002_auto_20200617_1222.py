# Generated by Django 3.0.7 on 2020-06-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldborder',
            name='fips',
            field=models.CharField(max_length=2, null=True, verbose_name='FIPS Code'),
        ),
    ]

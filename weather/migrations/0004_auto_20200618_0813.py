# Generated by Django 3.0.7 on 2020-06-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20200618_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='australianstates',
            name='offname',
            field=models.CharField(max_length=254, null=True),
        ),
    ]

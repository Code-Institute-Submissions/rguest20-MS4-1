# Generated by Django 3.2.3 on 2021-07-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20210718_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_updated',
            field=models.DateTimeField(null=True, verbose_name='Date Updated'),
        ),
    ]

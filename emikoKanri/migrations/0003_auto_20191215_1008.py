# Generated by Django 2.2.5 on 2019-12-15 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emikoKanri', '0002_auto_20191215_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurserecord',
            name='nurse_day',
            field=models.DateField(),
        ),
    ]

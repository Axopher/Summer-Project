# Generated by Django 4.0.4 on 2022-05-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0012_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='Admission',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='student',
            name='StPhone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='TPhone',
            field=models.BigIntegerField(),
        ),
    ]

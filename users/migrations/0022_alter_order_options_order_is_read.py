# Generated by Django 4.0.4 on 2022-09-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_product_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='order',
            name='is_read',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_alter_student_stgender_alter_teacher_tgender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StPhone',
            field=models.BigIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='TPhone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]

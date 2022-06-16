# Generated by Django 4.0.4 on 2022-05-02 16:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_rename_ctid_course_ctname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='TPhone',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StNum', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('StName', models.CharField(max_length=100)),
                ('StPhone', models.IntegerField()),
                ('StEmail', models.EmailField(max_length=254)),
                ('StAddress', models.CharField(max_length=100)),
                ('StDob', models.DateField()),
                ('StGender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'others')], max_length=6)),
                ('StRemarks', models.TextField()),
                ('StCName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminpanel.course')),
            ],
        ),
    ]

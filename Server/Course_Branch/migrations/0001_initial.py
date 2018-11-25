# Generated by Django 2.1.3 on 2018-11-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BRANCH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.CharField(max_length=5, unique=True)),
                ('branch_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='COURSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=40)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Course_Branch.BRANCH')),
            ],
        ),
    ]

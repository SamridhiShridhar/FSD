# Generated by Django 5.0.4 on 2024-06-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField(default='1900-01-01')),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('course_id', models.IntegerField(default=0, unique=True)),
                ('students', models.ManyToManyField(related_name='courses', to='course_registration.student')),
            ],
        ),
    ]
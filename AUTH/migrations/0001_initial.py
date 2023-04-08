# Generated by Django 4.2 on 2023-04-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Care_giver',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ID_number', models.IntegerField(blank=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
                ('surety_name', models.CharField(blank=True, max_length=254, null=True)),
                ('surety_IDnumber', models.CharField(blank=True, max_length=254, null=True)),
                ('years_of_exprience', models.IntegerField()),
                ('question', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('ID_number', models.IntegerField(blank=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

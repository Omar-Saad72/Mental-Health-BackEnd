# Generated by Django 4.0.5 on 2022-06-15 15:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='doctorlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=10, null=True)),
                ('specialty', models.CharField(default=None, max_length=50, null=True)),
                ('session_price', models.IntegerField(default=None, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='blog_images')),
                ('description', models.CharField(default=None, max_length=300, null=True)),
                ('freetime', models.ManyToManyField(to='doctors.availability')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration', models.CharField(choices=[('30mins', 'halfhour'), ('1', 'onehour'), ('2', 'twohour')], max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctors.doctorlist')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctors.user')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctorlist')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.user')),
            ],
        ),
    ]

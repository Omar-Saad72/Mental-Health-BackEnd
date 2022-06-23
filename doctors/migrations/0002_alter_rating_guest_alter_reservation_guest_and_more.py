# Generated by Django 4.0.5 on 2022-06-16 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]

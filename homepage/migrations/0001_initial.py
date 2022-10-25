# Generated by Django 4.1 on 2022-10-25 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinsi', models.CharField(max_length=60)),
                ('positive', models.BigIntegerField(default=0)),
                ('death', models.BigIntegerField(default=0)),
                ('recovered', models.BigIntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
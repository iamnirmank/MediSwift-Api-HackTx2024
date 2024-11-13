# Generated by Django 5.0.7 on 2024-11-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.TextField()),
                ('response_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('date_of_illness', models.DateField()),
                ('symptoms', models.TextField()),
                ('disease', models.CharField(max_length=200)),
                ('diagnosis', models.TextField()),
                ('medication', models.TextField()),
                ('frequency', models.CharField(max_length=100)),
                ('length_of_treatment', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 4.0.5 on 2023-05-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumos',
            fields=[
                ('idConsumos', models.AutoField(primary_key=True, serialize=False)),
                ('fechaMedicion', models.DateTimeField()),
                ('consumo', models.FloatField()),
            ],
        ),
    ]

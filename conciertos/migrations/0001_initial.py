# Generated by Django 4.2.1 on 2023-08-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concierto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'concierto',
                'verbose_name_plural': 'conciertos',
                'db_table': 'conciertos',
            },
        ),
    ]

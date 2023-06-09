# Generated by Django 4.1.7 on 2023-03-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_bookaseat'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookaSeatContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='User Name')),
                ('user_phone', models.CharField(max_length=35, verbose_name='User Phone Number')),
                ('user_time', models.TimeField(verbose_name='User Time')),
                ('user_place', models.CharField(max_length=30, verbose_name='User Place')),
                ('user_date', models.DateField(verbose_name='User Date')),
                ('user_text', models.TextField(verbose_name='User Text')),
            ],
        ),
        migrations.AlterField(
            model_name='bookaseat',
            name='subtitle',
            field=models.CharField(max_length=60, verbose_name='Book a Seat SubTitle'),
        ),
    ]

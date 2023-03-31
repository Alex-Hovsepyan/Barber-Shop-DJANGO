# Generated by Django 4.1.7 on 2023-03-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Sidebar Image')),
                ('home', models.CharField(max_length=25, verbose_name='Home')),
                ('about', models.CharField(max_length=25, verbose_name='About')),
                ('service', models.CharField(max_length=25, verbose_name='Services')),
                ('price', models.CharField(max_length=25, verbose_name='Price List')),
                ('contact', models.CharField(max_length=25, verbose_name='Contact')),
            ],
        ),
    ]
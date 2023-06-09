# Generated by Django 4.1.7 on 2023-03-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Service Content Image')),
                ('title', models.CharField(max_length=20, verbose_name='Service Content Title')),
                ('price', models.CharField(max_length=15, verbose_name='Service Content Price')),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='img',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Service Image'),
        ),
    ]

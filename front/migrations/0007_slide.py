# Generated by Django 4.1.1 on 2022-09-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
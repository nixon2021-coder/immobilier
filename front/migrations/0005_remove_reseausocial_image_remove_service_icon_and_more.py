# Generated by Django 4.1.1 on 2022-09-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_remove_reseausocial_icon_reseausocial_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reseausocial',
            name='image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Icon',
        ),
        migrations.AddField(
            model_name='reseausocial',
            name='Icon',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

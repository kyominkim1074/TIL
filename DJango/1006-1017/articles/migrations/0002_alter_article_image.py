# Generated by Django 3.2.13 on 2022-10-17 06:39

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]

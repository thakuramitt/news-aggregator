# Generated by Django 4.2.4 on 2023-09-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_newsarticle_author_newsarticle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

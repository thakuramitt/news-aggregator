# Generated by Django 4.2.4 on 2023-09-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_remove_newsarticle_id_newsarticle_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='uuid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
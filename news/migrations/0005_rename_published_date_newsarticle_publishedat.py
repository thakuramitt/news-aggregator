# Generated by Django 4.2.4 on 2023-09-05 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newsarticle_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='published_date',
            new_name='publishedAt',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mobile', '0002_remove_homonym_homonym_descriptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homonym',
            name='homonym_meaning',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

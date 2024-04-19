# Generated by Django 5.0.4 on 2024-04-19 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'WordGroups',
                'db_table': 'wordgroups',
            },
        ),
        migrations.CreateModel(
            name='Homonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homonym_name', models.CharField(max_length=150)),
                ('homonym_origin', models.CharField(max_length=100)),
                ('homonym_meaning', models.CharField(max_length=200)),
                ('homonym_descriptions', models.TextField()),
                ('homonym_example', models.TextField()),
                ('homonym_word_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mobile.wordgroup')),
            ],
            options={
                'verbose_name_plural': 'Homonyms',
                'db_table': 'homonyms',
            },
        ),
    ]
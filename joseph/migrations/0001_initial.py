# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-02 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_num', models.CharField(max_length=100)),
                ('original_word', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cases_validate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Misspelled', models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], default=False)),
                ('gene', models.CharField(max_length=200)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joseph.cases')),
            ],
        ),
        migrations.CreateModel(
            name='gene_in_CT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.CharField(db_index=True, max_length=200)),
                ('frequency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneSyn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.CharField(max_length=150)),
                ('synonyms', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='potential_gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joseph.gene_in_CT')),
            ],
        ),
        migrations.CreateModel(
            name='words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=200)),
                ('frequency', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='potential_gene',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joseph.words'),
        ),
        migrations.AddField(
            model_name='cases',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joseph.words'),
        ),
    ]

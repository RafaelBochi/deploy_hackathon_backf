# Generated by Django 4.2.3 on 2023-07-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_livro_data_pub_livro_paginas_livro_sinopse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='vendas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

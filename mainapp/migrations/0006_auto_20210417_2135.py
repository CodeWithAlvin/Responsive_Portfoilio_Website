# Generated by Django 3.1.7 on 2021-04-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210417_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

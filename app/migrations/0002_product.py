# Generated by Django 2.0.1 on 2018-01-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140)),
                ('unit_quantity', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('category', models.CharField(blank=True, max_length=140)),
                ('description', models.TextField(max_length=140)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-18 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140)),
                ('payment_mode', models.CharField(max_length=140)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('checked_out', models.BooleanField(default=False, verbose_name='checked out')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140)),
                ('description', models.CharField(blank=True, max_length=140)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='unit price')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('description', models.TextField(max_length=140)),
                ('object_id', models.PositiveIntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_buyer', to='app.Buyer')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='app.Cart')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app.Category')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comtent_type', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(blank=True, max_length=225)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='app.Buyer')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity', to='app.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140)),
                ('payment_mode', models.CharField(max_length=140)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='locatiom',
            new_name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='contract',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='app.Seller'),
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commodity',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_seller', to='app.Seller'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL),
        ),
    ]

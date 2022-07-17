# Generated by Django 3.2 on 2022-07-17 08:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='Category/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('sku', models.FloatField(verbose_name='SKU')),
                ('price', models.FloatField(verbose_name='price')),
                ('desc', models.TextField(max_length=1000, verbose_name='Desc')),
                ('flag', models.CharField(choices=[('new', 'new'), ('feature', 'feature')], max_length=10)),
                ('brand', models.ForeignKey(blank=b'I01\n', null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, related_name='products_brand', to='products.brand', verbose_name='brand')),
                ('category', models.ForeignKey(blank=b'I01\n', null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, related_name='products_category', to='products.category', verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000, verbose_name='Review')),
                ('rate', models.FloatField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Rate')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('product', models.ForeignKey(blank=b'I01\n', null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, related_name='product_review', to='products.products', verbose_name='Product')),
                ('user', models.ForeignKey(blank=b'I01\n', null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product/', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.products', verbose_name='Product')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-07-17 08:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=order.models.generated_code, max_length=8, verbose_name='Code')),
                ('order_status', models.CharField(choices=[('Received', 'Received'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=10, verbose_name='Order status')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Order time')),
                ('delivery_time', models.DateTimeField(blank=b'I01\n', null=b'I01\n', verbose_name='Delivery time')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Price')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_detail', to='order.order', verbose_name='Order')),
                ('product', models.ForeignKey(blank=b'I01\n', null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, related_name='order_procduct', to='products.product', verbose_name='Product')),
            ],
        ),
    ]

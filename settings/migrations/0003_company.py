# Generated by Django 3.2 on 2022-08-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20220803_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='company/')),
                ('about', models.CharField(max_length=300)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('tw_link', models.URLField(blank=True, null=True)),
                ('ins_link', models.URLField(blank=True, null=True)),
                ('email', models.URLField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-08-03 13:17

from django.db import migrations, models
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220801_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.generate_code.generated_code, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='code_used',
            field=models.BooleanField(default=False),
        ),
    ]

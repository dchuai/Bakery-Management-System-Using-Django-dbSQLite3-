# Generated by Django 3.2 on 2023-12-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakerystore', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(default='pending', max_length=128),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0010_remove_cartdb_cart_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('PIN', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_options_alter_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.SlugField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]

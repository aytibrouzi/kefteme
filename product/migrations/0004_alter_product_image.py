# Generated by Django 4.2 on 2023-04-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_created_data_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default2.jpg', upload_to='post_image/'),
        ),
    ]

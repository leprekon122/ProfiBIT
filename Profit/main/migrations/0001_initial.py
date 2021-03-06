# Generated by Django 4.0.3 on 2022-03-31 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=90)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('in_stock', 'in_stock'), ('out_of_stock', 'out_of_stock')], max_length=255)),
                ('remains', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': "Product's",
            },
        ),
    ]

# Generated by Django 3.0.5 on 2021-05-27 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cart', '0001_initial'),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.CartModel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.ProductModel')),
            ],
        ),
        migrations.AddConstraint(
            model_name='cartitemsmodel',
            constraint=models.UniqueConstraint(fields=('cart', 'product'), name='cartItem_key'),
        ),
    ]

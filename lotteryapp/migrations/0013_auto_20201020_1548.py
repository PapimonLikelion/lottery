# Generated by Django 3.1.2 on 2020-10-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotteryapp', '0012_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_date',
            field=models.DateField(default=None),
        ),
    ]
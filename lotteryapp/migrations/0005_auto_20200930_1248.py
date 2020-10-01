# Generated by Django 3.1.1 on 2020-09-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotteryapp', '0004_auto_20200930_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dicty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=240)),
                ('value', models.CharField(db_index=True, max_length=240)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotteryapp.dicty')),
            ],
        ),
        migrations.AlterField(
            model_name='dummyrequest',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotteryapp.dicty'),
        ),
    ]
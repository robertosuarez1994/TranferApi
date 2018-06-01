# Generated by Django 2.0.5 on 2018-05-30 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(null=True)),
                ('branchOffice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransferProductApp.BranchOffice')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransferProductApp.Product')),
            ],
        ),
    ]
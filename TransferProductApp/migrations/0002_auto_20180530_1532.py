# Generated by Django 2.0.5 on 2018-05-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TransferProductApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='branchOffice_id',
            new_name='branchOffice',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='product_id',
            new_name='product',
        ),
    ]

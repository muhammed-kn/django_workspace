# Generated by Django 3.2.5 on 2021-11-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211109_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='team',
            field=models.CharField(choices=[('Development', 'Development'), ('Product', 'Product'), ('Design', 'Design'), ('Human Resource', 'Human Resource')], max_length=50),
        ),
    ]

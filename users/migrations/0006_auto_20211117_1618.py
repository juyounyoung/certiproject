# Generated by Django 3.2.9 on 2021-11-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211117_1545'),
    ]

    operations = [

        # migrations.AddField(
        #     model_name='user',
        #     name='school_address',
        #     field=models.CharField(max_length=20, null=True, verbose_name='학교주소'),
        # ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(auto_created=True, primary_key=False, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_id',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='학교이름'),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users','0001_initial'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='user',
        #     name='account_id',
        # ),
        migrations.AddField(
            model_name='user',
            name='account_id',
            field=models.CharField(default='', max_length=20, primary_key=False, serialize=False, verbose_name='학교이름'),
        ),
    ]

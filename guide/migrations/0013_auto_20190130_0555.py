# Generated by Django 2.1.5 on 2019-01-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0012_auto_20190129_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservices',
            name='total_cost',
            field=models.IntegerField(help_text='In nRs', null=True),
        ),
    ]

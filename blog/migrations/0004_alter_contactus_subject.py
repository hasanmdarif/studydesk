# Generated by Django 3.2 on 2021-05-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contactus_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 3.1 on 2020-10-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200919_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='username',
            field=models.CharField(max_length=150, null=True, verbose_name='Username'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-07 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20200307_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='palabrasclave',
            old_name='palabrasClave',
            new_name='id_palabrasClave',
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_palabrasclave_palabrasclave'),
    ]

    operations = [
        migrations.AddField(
            model_name='palabrasclave',
            name='palabra',
            field=models.CharField(default='', help_text='Respuesta del servidor', max_length=500),
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.IntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Noche')], default=1),
        ),
    ]
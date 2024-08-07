# Generated by Django 5.0.8 on 2024-08-07 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finertia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('alltransactions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finertia.alltransactions')),
                ('card_number', models.IntegerField(max_length=20)),
                ('cvv_number', models.IntegerField(max_length=3)),
            ],
            bases=('finertia.alltransactions',),
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-07 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finertia', '0002_customuser_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('alltransactions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finertia.alltransactions')),
                ('card_number', models.IntegerField(max_length=16)),
                ('cvv_number', models.IntegerField(max_length=3)),
            ],
            bases=('finertia.alltransactions',),
        ),
    ]

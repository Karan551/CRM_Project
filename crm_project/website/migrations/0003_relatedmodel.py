# Generated by Django 5.0.7 on 2024-07-28 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_record_contact_number_alter_record_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.record')),
            ],
        ),
    ]

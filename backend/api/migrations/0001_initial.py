# Generated by Django 3.1.3 on 2020-11-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('radius', models.IntegerField(blank=True, default=0)),
                ('upvotes', models.IntegerField(blank=True, default=0)),
                ('variant', models.CharField(choices=[('RD', 'Road'), ('SL', 'StreetLight'), ('PW', 'PublicWashroom'), ('SW', 'Sewage'), ('GB', 'Garbage'), ('OR', 'Other')], default='RD', max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('typology_one', models.CharField(blank=True, default='', max_length=500, verbose_name='Typology One')),
                ('typology_two', models.CharField(blank=True, default='', max_length=500, verbose_name='Typology Two')),
                ('total', models.FloatField(blank=True, default=None, null=True, verbose_name='Total')),
                ('health_points', models.FloatField(blank=True, default=None, null=True, verbose_name='HP')),
                ('attack', models.FloatField(blank=True, default=None, null=True, verbose_name='Attack')),
                ('defense', models.FloatField(blank=True, default=None, null=True, verbose_name='Defense')),
                ('special_attack', models.FloatField(blank=True, default=None, null=True, verbose_name='Special attack')),
                ('special_defense', models.FloatField(blank=True, default=None, null=True, verbose_name='Special defense')),
                ('speed', models.FloatField(blank=True, default=None, null=True, verbose_name='Speed')),
                ('is_legendary', models.BooleanField(default=False, verbose_name='Legendary')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokedex',
            },
        ),
    ]

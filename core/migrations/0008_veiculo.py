# Generated by Django 2.1.1 on 2018-09-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('cor', models.CharField(max_length=15)),
                ('ano', models.IntegerField()),
                ('placa', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]

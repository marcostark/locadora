# Generated by Django 2.1.1 on 2018-09-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=15)),
                ('status', models.TextField()),
                ('pontos_fidelidade', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]

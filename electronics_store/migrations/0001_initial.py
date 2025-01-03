# Generated by Django 4.2 on 2024-11-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Название')),
                ('level', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], verbose_name='Сетевой уровень')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Задолженность перед поставщиком')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='electronics_store.networkmember', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'элемент в сети',
                'verbose_name_plural': 'сетевые элементы',
                'ordering': ['level'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название продукта')),
                ('model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Модель')),
                ('release_date', models.DateField()),
                ('selling_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics_store.networkmember')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ['name', 'release_date'],
            },
        ),
        migrations.CreateModel(
            name='ContactsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома')),
                ('base_class', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='electronics_store.networkmember')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]

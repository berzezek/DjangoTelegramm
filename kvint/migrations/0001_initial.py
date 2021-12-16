# Generated by Django 4.0 on 2021-12-15 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в сети')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя ')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения заказа')),
                ('order_msg', models.CharField(default='', max_length=255, verbose_name='Размер пиццы')),
                ('payment_msg', models.CharField(default='', max_length=255, verbose_name='Размер пиццы')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kvint.profile', verbose_name='Профиль')),
            ],
        ),
    ]
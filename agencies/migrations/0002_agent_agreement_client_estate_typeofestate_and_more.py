# Generated by Django 5.1.2 on 2024-11-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('credit', models.CharField(max_length=100, verbose_name='Контактные данные')),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('agent_Id', models.IntegerField(verbose_name='Кол агента')),
                ('client_Id', models.IntegerField(verbose_name='Кол клиента')),
                ('estate_Id', models.IntegerField(verbose_name='Код недвижимости')),
                ('payment_type_Id', models.IntegerField(verbose_name='Код формы оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('type_dealer', models.CharField(max_length=20, verbose_name='Тип участника сделки')),
                ('passport', models.CharField(max_length=50, verbose_name='Паспортные данные')),
                ('credit', models.CharField(max_length=100, verbose_name='Контактные данные')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SmallIntegerField(verbose_name='Тип недвижимости')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('cadastral_number', models.CharField(max_length=50, verbose_name='Кадастровый номер')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
            ],
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
    ]

from django.db import models
from django.urls import reverse

class Agent(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    credit = models.CharField(verbose_name="Контактные данные", max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    type_dealer = models.CharField(verbose_name="Тип участника сделки", max_length=20)
    passport = models.CharField(verbose_name="Паспортные данные", max_length=50)
    credit = models.CharField(verbose_name="Контактные данные", max_length=100)

    def get_absolute_url(self): 
        return reverse('client', kwargs={'cl_id': self.pk})


class TypeOfPayment(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=30)


class TypeOfEstate(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=30)


class Estate(models.Model):
    name = models.SmallIntegerField(verbose_name="Тип недвижимости")
    address = models.CharField(verbose_name="Адрес", max_length=150)
    cadastral_number = models.CharField(verbose_name="Кадастровый номер", max_length=50)


class Agreement(models.Model):
    price = models.IntegerField(verbose_name="Стоимость")
    agent_Id = models.IntegerField(verbose_name="Агент")
    client_Id = models.IntegerField(verbose_name="Клиент")
    estate_Id = models.IntegerField(verbose_name="Недвижимость")
    payment_type_Id = models.IntegerField(verbose_name="Формы оплаты")

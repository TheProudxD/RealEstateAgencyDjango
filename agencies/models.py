from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Agent(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    credit = models.CharField(verbose_name="Контактные данные", max_length=100)
    photo = models.ImageField(verbose_name="Фото", upload_to=r"photos/%Y/%m/%d/")
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE, verbose_name='Договор', related_name='get_agents', null=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): 
        return reverse('agent', kwargs={'ag_slug': self.slug})
    
    class Meta: 
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'
        ordering = ['id', 'name']


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    type_dealer = models.CharField(verbose_name="Тип участника сделки", max_length=20)
    passport = models.CharField(verbose_name="Паспортные данные", max_length=50)
    credit = models.CharField(verbose_name="Контактные данные", max_length=100)
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE, verbose_name='Договор', null=True)

    def get_absolute_url(self): 
        return reverse('client', kwargs={'cl_id': self.pk})
    
    class Meta: 
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TypeOfPayment(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=30)
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE, verbose_name='Договор', null=True)

    class Meta: 
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'


class TypeOfEstate(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=30)
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE, verbose_name='Договор', null=True)

    class Meta: 
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

class Estate(models.Model):
    name = models.SmallIntegerField(verbose_name="Тип недвижимости")
    address = models.CharField(verbose_name="Адрес", max_length=150)
    cadastral_number = models.CharField(verbose_name="Кадастровый номер", max_length=50)

    class Meta: 
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'


class Agreement(models.Model):
    price = models.IntegerField(verbose_name="Стоимость")

    def __str__(self):
        return "Договор " + str(self.id)

    class Meta: 
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f"Сообщение от {self.name}"
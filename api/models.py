from django.db import models
from datetime import datetime

#Table User
class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10 , default="")
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES , default=0, editable = False)
    date_of_birthday = models.DateField(default = datetime.now)
    STATE_BLOCKED = 0
    STATE_ACTIVE = 1
    STATE_CHOICES = [(STATE_ACTIVE, "Activo"), (STATE_BLOCKED, "Bloqueado")]
    state = models.IntegerField(choices=STATE_CHOICES, default=1)
    user = models.CharField(max_length=50, default = name)
    date_register = models.DateField(default = datetime.now,  editable = False)
    date_modify = models.DateField(default = datetime.now)
    longitude_home = models.FloatField(default = 0)
    latitude_home = models.FloatField(default = 0)

    def __str__(self):
        return self.id

class Client(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField(default = datetime.now)

    def __str__(self):
        return self.id

class Employee(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField(default = datetime.now)
    charge = models.CharField(max_length=50)

    def __str__(self):
        return self.id

class Area(models.Model):
    employee_register = models.ForeignKey(Employee, related_name = "employee_register", on_delete=models.PROTECT)
    employee_modify = models.ForeignKey(Employee, related_name = "employee_modify", on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    STATE_INACTIVE = 0
    STATE_ACTIVE = 1
    STATE_CHOICES = [(STATE_ACTIVE, "Activo"), (STATE_INACTIVE, "Inactivo")]
    state = models.IntegerField(choices=STATE_CHOICES, default=1)
    date_register = models.DateField(default = datetime.now,  editable = False)
    date_modify = models.DateField(default = datetime.now)

    def __str__(self):
        return self.id

class AddressClient(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    address = models.CharField(max_length=50)
    reference = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_register = models.DateField(default = datetime.now,  editable = False)
    date_modify = models.DateField(default = datetime.now)

    def __str__(self):
        return self.id



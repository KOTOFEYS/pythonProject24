from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    num_tel = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    # num_tel = models.BigIntegerField(max_length=16)

    def __str__(self):
        return self.name
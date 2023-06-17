from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.country_name
class Capital(models.Model):
    country_name = models.OneToOneField(Country,on_delete=models.CASCADE)
    Capital_city = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Capital_city
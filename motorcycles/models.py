from django.db import models

# Create your models here.

class Bike(models.Model):
    name = models.CharField(max_length = 20)
    review = models.CharField(max_length = 200, null=True,blank=True)
    className = models.CharField(max_length = 30, null=True)
    topSpeed = models.CharField(max_length=15, null=True)
    releaseDate = models.DateField()
    designer_name = models.CharField(max_length = 50, blank=True)
    nationality = models.CharField(max_length = 30, blank=True)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    brandName = models.CharField(max_length = 20,blank=True)
    p_country =  models.CharField(max_length = 30,blank=True) # p_country is production country
    website = models.URLField(blank=True)
    bikeModel = models.ForeignKey(Bike)

    def __str__(self):
        return self.brandName

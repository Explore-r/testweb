from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.IntegerField()
    Medical_Status = models.CharField(max_length=200,null=True)
    Earning = models.FloatField()

    def _str_(self):
        return self.name
    

class Product (models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    Artist = models.ForeignKey(Person,null=True,on_delete=models.SET_NULL)
    def _str_(self):
        return self.name
    

class Resources (models.Model):
    Equipment = models.CharField(max_length=200, null=True)
    Raw_Material = models.CharField(max_length=200, null=True)
    Available = models.IntegerField()
    Required = models.IntegerField()
    

# class Donations (models.Model):
#     ORGANISATION=(
#         ('Private','Private'),
#         ('Government','Government'),
#         ('NGO','NGO'),

#     )




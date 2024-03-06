from django.db import models

# Create your models here.
class Domicile(models.Model):
    street = models.CharField(max_length = 255)
    street_number = models.IntegerField()
    country = models.CharField(max_length = 255)

    def __str__(self):
        return f'Domicile {self.id}: {self.street} {self.street_number} {self.country}'
class People(models.Model): #all model classes in django have to extend from a father class called models.Model
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    domicile = models.ForeignKey(Domicile, on_delete = models.SET_NULL, null = True) # on delete = what happens if you delete an atribute from Domicile

    def __str__(self):
        return f'Persona {self.id}: {self.name} {self.surname} {self.email}'

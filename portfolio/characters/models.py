from django.db import models

class Character(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  strength = models.IntegerField(null=True)
  dexterity = models.IntegerField(null=True)
  constitution = models.IntegerField(null=True)
  intelligence = models.IntegerField(null=True)
  wisdom = models.IntegerField(null=True)
  charisma = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
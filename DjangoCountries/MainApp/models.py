from django.db import models

class Language(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self):
      return f'Language: {self.name}'

class Item(models.Model):
   country = models.CharField(max_length=100)
   language = models.ManyToManyField(to=Language)

   def __repr__(self):
      return f'Item: {self.country}'
   

from django.db import models
class Knjiga(models.Model):
	naslov = models.text
	autor = models.IntegerField
class Slika(models.Model):
	ime = models.text
	falsifikat? = models.boolean
class Film(models.Model):
	naziv = models.text
	autor = models.CharField

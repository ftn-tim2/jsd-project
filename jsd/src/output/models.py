from django.db import models
class Knjiga(models.Model):
	naslov = models.TextField()
	autor = models.IntegerField()
	
	def __unicode__(self):
		return self.naslov    

class Slika(models.Model):
	ime = models.TextField(null=True,default="ime")
	falsifikat = models.BooleanField()
	
	def __unicode__(self):
		return self.ime    

class Film(models.Model):
	naziv = models.TextField()
	autor = models.CharField(null=False,max_length=80)
	knjiga = models.ForeignKey(Knjiga)
	
	def __unicode__(self):
		return self.naziv    


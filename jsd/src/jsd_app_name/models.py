from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    title = models.TextField()
    author = models.IntegerField(default=90)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jsd_app_name:book_edit', kwargs={'pk': self.pk})


class Picture(models.Model):
    name = models.TextField(null=True, default="ime")
    fake = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jsd_app_name:picture_edit', kwargs={'pk': self.pk})


class Film(models.Model):
    title = models.TextField()
    author = models.CharField(null=False, max_length="80")
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jsd_app_name:film_edit', kwargs={'pk': self.pk})



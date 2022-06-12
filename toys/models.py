from django.db import models

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=100, blank=False, default='')
  description = models.TextField(max_length=250, blank=True, default='')
  created = models.DateTimeField(auto_now_add=True)
  toy_category = models.CharField(max_length=200, blank=False, default='')
  release_date = models.DateTimeField()
  was_home = models.BooleanField(default=False)

  class Meta:
    ordering = ("name",)
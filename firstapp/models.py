from django.db import models

# the following lines added:
import datetime
from django.utils import timezone

class Topic(models.Model):
   top_name = models.CharField(max_length=200,unique=True)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.top_name

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    area=models.CharField(max_length=200,default=0)
    name=models.CharField(max_length=200,default=0)
    work=models.CharField(max_length=200,default=0)
    number=models.IntegerField(max_length=200,default=0)
    def __str__(self):
        return str(self.name)
class InputUser(models.Model):
    name=models.CharField(max_length=200,default=0)
    email=models.EmailField(max_length=200,default=0)
    area=models.CharField(max_length=200,default=0)
    field=models.CharField(max_length=200,default=0)
    def __str__(self):
        return str(self.name)

from django.db import models

# Create your models here.
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    date     = models.DateField()
    location = models.CharField(max_length=40)
    notes    = models.TextField(null=True, blank=True)
 
    def get_absolute_url(self):
        return reverse("events:events-detail", kwargs={"id": self.id}) #f"/user/{self.id}/" # app_name::name in urls.py
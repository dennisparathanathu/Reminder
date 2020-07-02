from django.db import models
from django.conf import settings



import _datetime


# Create your models here.
class Reminder(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    current_date=models.DateTimeField(default=_datetime.datetime.now())
    reminder_date=models.DateTimeField(default=_datetime.datetime.now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


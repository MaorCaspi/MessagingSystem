from asyncio import SendfileNotAvailableError
from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=10)
    receiver = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    creationDate = models.DateField
    beenRead = models.BooleanField
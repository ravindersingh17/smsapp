from django.db import models

# Create your models here.

class Sms(models.Model):
    from_num = models.CharField(max_length = 15)
    message = models.CharField(max_length = 2800)
    message_id = models.CharField(max_length = 20)
    sent_to = models.CharField(max_length = 15)
    secret = models.CharField(max_length = 20)
    device_id = models.CharField(max_length = 10, default="")
    sent_timestamp = models.IntegerField()

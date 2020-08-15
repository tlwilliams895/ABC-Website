from django.db import models


# Create your models here.
class Join(models.Model):
    name = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)

    class Meta:
        db_table = "ContactUs"

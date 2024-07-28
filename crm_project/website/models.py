from django.db import models


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RelatedModel(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

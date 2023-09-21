from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.FloatField()
    organization =models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=1000)

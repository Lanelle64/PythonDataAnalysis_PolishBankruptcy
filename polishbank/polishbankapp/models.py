from django.db import models

class PolishBank(models.Model):
    # Your model fields go here
    field1 = models.CharField(max_length=255)
    field2 = models.FloatField()
    # Add other fields as needed

    class Meta:
        app_label = 'polishbankapp'

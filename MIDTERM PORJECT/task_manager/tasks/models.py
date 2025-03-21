from django.db import models

# Create your models here.

class Field(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} {self.description} {self.due_date} {self.status}"
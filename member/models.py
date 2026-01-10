from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    membership_date = models.DateField()

    def __str__(self):
        return self.name
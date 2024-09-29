from django.db import models

class Authors(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100, unique=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=3, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

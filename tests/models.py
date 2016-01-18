from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

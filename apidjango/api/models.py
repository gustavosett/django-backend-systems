from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25, blank=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.login

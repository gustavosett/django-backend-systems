from django.db import models


class Login(models.Model):
    nickname = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=120)

    class Meta:
        db_table = "Login"

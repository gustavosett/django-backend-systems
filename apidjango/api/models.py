from django.db import models


class Login(models.Model):
    nickname = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=25)

    class Meta:
        db_table = "Login"

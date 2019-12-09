from __future__ import unicode_literals
from django.db import models
import re
# from django.core.validators import validate_email

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User Last name should be at least 2 characters"
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
            errors["email"] = "Email not valid"
        if len(postData['password']) < 8:
            errors["password"] = "User password should be at least 8 characters"
        return errors
    def login_validator(self, postData):
        errors = {}
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
            errors["email"] = "Email not valid"
        if len(postData['password']) < 8:
            errors["password"] = "User password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    objects = UserManager()

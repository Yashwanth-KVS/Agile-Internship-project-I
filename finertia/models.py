from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.conf import settings  # For accessing the custom user model


class AllTransactions(models.Model):
    date = models.DateTimeField()
    mode = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_expense = models.CharField(max_length=20)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount} {self.currency}"


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(AllTransactions)

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions', blank=True)

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_field1 = models.CharField(max_length=255, blank=True)
    additional_field2 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Card(AllTransactions):
    card_number = models.IntegerField(max_length=16)
    cvv_number = models.IntegerField(max_length=3)

    def __str__(self):
        return f"{self.card_number} - {self.cvv_number}"

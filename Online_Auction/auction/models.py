from django.db import models

# Create your models here.
class Bidder(models.model):
    name = models.CharField(max_length=60),


class Result(models.model):
    name = models.CharField(max_length=60),

class Payment(models.model):
    name = models.CharField(max_length=60),

class Member_fee(models.model):
    name = models.CharField(max_length=60),

class Status(models.model):
    name = models.CharField(max_length=60),

class Send_Feedback(models.model):
    name = models.CharField(max_length=60),

class Auction_User(models.model):
    name = models.CharField(max_length=60),

class Category(models.model):
    name = models.CharField(max_length=60),

class Sub_Category(models.model):
    name = models.CharField(max_length=60),

class Session_date(models.model):
    name = models.CharField(max_length=60),

class Session_Time(models.model):
    name = models.CharField(max_length=60),

class Product(models.model):
    name = models.CharField(max_length=60),

class Aucted_Product(models.model):
    name = models.CharField(max_length=60),

class Participant(models.model):
    name = models.CharField(max_length=60),




from django.db import models

# Create your models here.

class Bidder(models.Model):
    name = models.CharField(max_length=60)
    product = models.CharField(max_length=60)


class Result(models.Model):
    name = models.CharField(max_length=60)


class Payment(models.Model):
    name = models.CharField(max_length=60)

class Member_fee(models.Model):
    price = models.IntegerField()


class Status(models.Model):
    name = models.CharField(max_length=60)


class Send_Feedback(models.Model):
    name = models.CharField(max_length=60)
    email =models.EmailField( max_length=254)
    message = models.TextField()


class Auction_User(models.Model):
    name = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=60)


class Sub_Category(models.Model):
    name = models.CharField(max_length=60)


class Session_date(models.Model):
    Date = models.DateField(max_length=60)


class Session_Time(models.Model):
    Time = models.TimeField(max_length=60)


class Product(models.Model):
    name = models.CharField(max_length=60)
    


class Aucted_Product(models.Model):
    name = models.CharField(max_length=60)


class Participant(models.Model):
    name = models.CharField(max_length=60)
    
from django.db import models

# Create your models here.

class Bidder(models.Model):
    user = models.ForeignKey()
    address = models.CharField(max_length=60)
    phone_number = models.IntegerField(max_length=20)
    bidding_limit = models.DecimalField()


class Result(models.Model):
    name = models.CharField(max_length=60)
    product = models.ForeignKey()
    winning_bid = models.DecimalField()
    winner = models.ForeignKey(Bidder)
    auction_end_time = models.DateTimeField()

class Payment(models.Model):
    payment_id = models.CharField()
    bidder = models.ForeignKey(Bidder)
    amount = models.DecimalField()
    payment_date = models.DateTimeField()
    status = models.CharField('pending , completaed')


class Member_fee(models.Model):
    auction_user = models.ForeignKey(Auction_User)
    fee_amount = models.DecimalField()
    due_date = models.DateTimeField()
    status = models.CharField()



class Status(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()



class Send_Feedback(models.Model):
    user = models.ForeignKey(Bidder)
    message = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField()



class Auction_User(models.Model):
   user = models.OneToOneField(Bidder)
   is_verified = models.BooleanField()
   profile_picture = models.ImageField()
   join_date = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()



class Sub_Category(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category)
    description = models.TextField()


class Session_date(models.Model):
    Date = models.DateField(max_length=60)
    is_holiday = models.BooleanField()



class Session_Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    timezone = models.CharField((""), max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    starting_bid = models.DecimalField((""), max_digits=5, decimal_places=2)
    category = models.ForeignKey("app.Model", verbose_name=("Category"), on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_Category)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

    


class Aucted_Product(models.Model):
    product = models.ForeignKey(Product)
    final_bid = models.DecimalField()
    winner = models.ForeignKey(Bidder)
    auction_date = models.DateTimeField()



class Participant(models.Model):
    auction = models.ForeignKey()
    bidder = models.ForeignKey(Bidder)
    participation_fee = models.DecimalField()
    is_active = models.BooleanField()
    
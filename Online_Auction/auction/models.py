from django.db import models

# Create your models here.

class Bidder(models.Model):
    User = models.CharField(("User"), max_length=50)
    address = models.CharField(max_length=60)
    phone_number = models.IntegerField()
    bidding_limit = models.DecimalField(("Bidding Limit"), max_digits=5, decimal_places=2)


class Result(models.Model):
    name = models.CharField(max_length=60)
    product = models.ForeignKey("auction.Product", verbose_name=("Product"), on_delete=models.CASCADE)
    winning_bid = models.DecimalField(("The Winning Bid"), max_digits=5, decimal_places=2)
    winner = models.ForeignKey("auction.Bidder", verbose_name=("Winner"), on_delete=models.CASCADE)
    auction_end_time = models.DateTimeField()

class Payment(models.Model):
    payment_id = models.CharField(("Payment Identity"), max_length=50)
    bidder = models.ForeignKey("auction.Bidder", verbose_name=("Bidder"), on_delete=models.CASCADE)
    amount = models.DecimalField(("Amount"), max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    status = models.CharField(("pending , completed"), max_length=50)


class Member_fee(models.Model):
    auction_user = models.ForeignKey("auction.Auction_User", verbose_name=("Auction User"), on_delete=models.CASCADE)
    fee_amount = models.DecimalField(("Amount"), max_digits=5, decimal_places=2)
    due_date = models.DateTimeField()
    status = models.CharField(("Status"), max_length=50)



class Status(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()



class Send_Feedback(models.Model):
    user = models.ForeignKey("auction.Bidder", verbose_name=("User"), on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField()



class Auction_User(models.Model):
   user = models.OneToOneField("auction.Bidder", verbose_name=("User"), on_delete=models.CASCADE)
   is_verified = models.BooleanField()
   profile_picture = models.ImageField()
   join_date = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()



class Sub_Category(models.Model):
    Name = models.CharField(max_length=60)
    category = models.ForeignKey("auction.Category", verbose_name=("Category"), on_delete=models.CASCADE)
    description = models.TextField()


class Session_date(models.Model):
    Date = models.DateField(max_length=60)
    is_holiday = models.BooleanField()



class Session_Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    timezone = models.CharField(("Current Zone"), max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    starting_bid = models.DecimalField(("Start Bid"), max_digits=5, decimal_places=2)
    category = models.ForeignKey("auction.Category", verbose_name=("Category"), on_delete=models.CASCADE)
    subcategory = models.ForeignKey("auction.Sub_Category", verbose_name=("Sub Category"), on_delete=models.CASCADE)
    image = models.ImageField(("Product Image"), upload_to=None, height_field=None, width_field=None, max_length=None)

    


class Aucted_Product(models.Model):
    product = models.ForeignKey("auction.Product", verbose_name=("Product"), on_delete=models.CASCADE)
    winner = models.ForeignKey("auction.Bidder", verbose_name=("Winner"), on_delete=models.CASCADE)
    final_bid = models.DecimalField(("Final Bid"), max_digits=5, decimal_places=2)
    auction_date = models.DateTimeField()



class Participant(models.Model):
    auction = models.ForeignKey("auction.Product", verbose_name=("Auction"), on_delete=models.CASCADE)
    bidder = models.ForeignKey("auction.Bidder", verbose_name=("user"), on_delete=models.CASCADE)
    participation_fee = models.DecimalField(("Activity Fee"), max_digits=5, decimal_places=2)
    is_active = models.BooleanField()
    
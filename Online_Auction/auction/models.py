from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_profile(models.Model):
    user_roles = (
        ('auctioner', 'Auctioner'),
        ('bidder', 'Bidder'),
    )

    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    role = models.CharField(("Role"), max_length=50, choices=user_roles)
    address = models.CharField(("Address"), max_length=50)
    business_name = models.CharField(("Business Name"), max_length=50, blank=True, null=True)
    verified = models.BooleanField(("verified"), default=False)


    def __str__(self):
        return f"{self.user.username} - {self.role}"
    


class auction(models.Model):
    title = models.CharField(("Title"), max_length=50)
    description = models.TextField(("Description"))
    starting_price = models.DecimalField(("Start-Price"), max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(("Created At"), auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(("Start Date"), auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(("End Date"), auto_now=False, auto_now_add=False)
    owner = models.ForeignKey("auction.user_profile", verbose_name=("Owner"), on_delete=models.CASCADE)
    is_active = models.BooleanField(("Online"), default=True)


    def __str__(self):
        return self.title
    

class bid(models.Model):
    auction = models.ForeignKey("auction.auction", verbose_name=("Auction"), on_delete=models.CASCADE)
    bidder = models.ForeignKey("auction.user_profile", verbose_name=("Bidder"), on_delete=models.CASCADE)
    bid_amount = models.DecimalField(("Bid-Amount"), max_digits=5, decimal_places=2)
    submited_at = models.DateTimeField(("Submitted At"), auto_now=False, auto_now_add=True)


    def __str__(self):
        return (
            f"{self.bidder.user.username}"
            f"{self.auction.title}"
            f"{self.bid_amount}"
        )
    


class watchlist(models.Model):
    user = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE)
    auction = models.ForeignKey("auction.auction", verbose_name=(""), on_delete=models.CASCADE)
    added_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.auction.title}"
    


class payment(models.Model):
    auction = models.OneToOneField("auction.auction", verbose_name=(""), on_delete=models.CASCADE)
    bidder = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE)
    amount = models.DecimalField((""), max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    status = models.CharField((""), max_length=50, choices=(('pending','Pending'), ('completed', 'Completed')))

    def __str__(self):
        return f"{self.bidder.user.username} - {self.auction.title} - {self.amount}"
    


class review(models.Model):
    reviewer = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE, related_name = 'received_reviews')
    rating = models.IntegerField((""), choices=(('1','1'), ('2','2'), ('3','3'),('4','4'),('5','5')))
    comment = models.TextField((""))
    created_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.reviewer.user.username} -> {self.reviewed_user.user.username} - {self.rating}"
    

class notification(models.Model):
    user = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE)
    message = models.TextField((""))
    is_read = models.BooleanField((""), default=False)
    created_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)


    def __str__(self):
        return f"{self.user.user.username} - {self.message[:20]}"
    


class message(models.Model):
    sender = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE)
    receiver = models.ForeignKey("auction.user_profile", verbose_name=("Reciever"), on_delete=models.CASCADE, related_name = 'received text')
    message = models.TextField((""))
    sent_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.sender.user.username} -> {self.receiver.user.username}"
    


class escrow(models.Model):
    auction = models.OneToOneField("auction.auction", verbose_name=(""), on_delete=models.CASCADE, related_name = 'escrow')
    bidder = models.ForeignKey("auction.user_profile", verbose_name=(""), on_delete=models.CASCADE, related_name='escrows')
    amount = models.DecimalField((""), max_digits=5, decimal_places=2)
    release_status = models.BooleanField((""), default=False)
    created_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Escrow for:{self.auction.title} - {self.amount}"
    



    
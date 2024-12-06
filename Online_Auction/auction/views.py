from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.forms import ModelForm
from django.contrib import messages
from .forms import RegisterForm





today=date.today()

# USER AUTHENTICATION VIEW
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()

           user_profile.objects.create(user = user, role = 'bidder')

        login(request, user)
        return redirect('home')
    else:
            form = RegisterForm()
            return render(request, 'accounts/register.html', {'form':form})



  
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'

            return redirect(next_url)
        
        else:
            error_message = "Invalid Credentials"

    return render(request, 'accounts/login.html', {'error':error_message})




def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('registration/registration.html')
    



@login_required
def profile(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, './pages/profile.html', context )







#HOMEPAGE & LISTINGS
def list_auctions(request):
    auctions = auction.objects.filter(status = 'active')
    context = {'auctions':auctions}
    return render(request, 'auction_list.html', context)


# AUCTION MANAGEMENT
    #auction details
def auction_detail(request, auction_id):
    auction = get_object_or_404(auction, id = auction_id)
    context = {'auction':auction}
    return render(request, 'auction_detail.html',context)




#CREATING AUCTION
class auction_form(ModelForm):
    class Meta:
        model = auction
        fields = ['title', 'description', 'starting_price', 'start_date','end_date']

@login_required
def create_auction(request):
    if request.method == 'POST':
        form = auction_form(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.auctioner = request.user.profile
            auction.save()
            return redirect('list_auctions')
    else:
        form = auction_form()
        context = {'form':form}
        return render (request, 'create_auction.html', context)




#BIDDING
@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(auction, id = auction_id)

    if request.method =='POST':
        bid_amount = request.POST.get('bid_amount')
        if float(bid_amount) > auction.current_price:
            bid.objects.create(
                auction = auction,
                bidder = request.user.profile,
                bid_amount =bid_amount
            )
            auction.current_price = bid_amount
            auction.save()
            messages.success(request, 'Bid placed successfully.')

        else:
            messages.error(request, 'Bid must be higher than the current prie.')

    return redirect('auction_detail', auction_id = auction.id)


#VIEW USER BIDS
@login_required
def my_bids(request):
    bids = bid.objects.filter(bidder = request.user.profile)
    context = {'bids':bids}
    return render(request, 'my_bids.html', context )


#WATCHLIST AND NOTIFICATIONS
@login_required
def notifications(request):
    notifications = request.user.profile.notifications.all()
    context = {"notifications":notifications}
    return render (request, 'notifications.html', context)


#WATCHLIST ADDITION
@login_required
def add_to_watchlist(request, auction_id):
    auction = get_object_or_404(auction, id = auction_id)

    watchlist.objects.get_or_create(user = request.user.profile, auction = auction)
    return redirect('auction_detail',auction_id = auction.id)


#WATCHLIST VEIWING
@login_required
def watchlist(request):
    Watchlist = watchlist.objects.filter(user = request.user.profile)
    context = {'Watchlist':Watchlist}
    return render(request, 'watchlist.html', context)



#PAYMENT AND CHECKOUT
@login_required
def payment_checkout(request, auction_id):
    auction = get_object_or_404(auction, id = auction_id)

    if auction.status != 'completed':
        return redirect('auction_detail', auction_id = auction.id)
    
    if request.method =='POST':
        payment.objects.create(
            auction = auction,
            bidder = request.user.profile,
            amount = auction.current_price,
            status = 'completed'
        )
        auction.status = 'completed'
        auction.save()
        return redirect('my_bids')
    context = {'auction':auction}
    return render (request, 'process_payment.html', context)


#REVIEW VIEWS FOR USERS
class review_form(ModelForm):
    class Meta:
        model = review
        fields = ['rating', 'comment']

@login_required
def leave_review(request, user_id):
    reviewed_user = get_object_or_404(user_profile, id = user_id)
    
    if request.method == "POST":
        form = review_form(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user.profile
            review.reviewed_user = reviewed_user
            review.save()
            return redirect('profile',user_id = reviewed_user.user.id)
    else:
        form = review_form()
    context = {'form':form, 'reviewed_user': reviewed_user}
    return render(request, 'leave_review.html', context,)







#ADMIN VIEW FOR DISPUTE MANAGEMENT
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    auctions = auction.objects.all()
    users = user_profile.objects.all()

    context = {'auctions':auctions, 'users':users}

    return render(request, 'admin_dashboard.html', context)


#SEARCH AND FILTERING
def search_filtering(request):
    pass


#AUCTION STATUS AND CLOSING
def auction_status(request):
    pass




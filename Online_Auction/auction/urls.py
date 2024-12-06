from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('auctions/', views.list_auctions, name='list_auctions'),
    path('auction/', views.auction_detail, name='auction_detail'),
    path('auction/create/', views.create_auction, name='create_auction'),
    path('auction/<int:auction_id>/bid/', views.place_bid, name='place_bid'),
    path('bids/', views.my_bids, name='my_bids'),
    path('notifications/', views.notifications, name='notifications'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/add/<int:auction_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('review/<int:user_id>/', views.leave_review, name='leave_review'),
    path('payment/<int:auction_id>/', views.payment_checkout, name='process_payment'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

]





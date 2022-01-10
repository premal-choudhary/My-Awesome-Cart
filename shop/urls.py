# from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About"),
    path('basic/', views.basic, name="Basic"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('tracker/', views.tracker, name="tracking status"),
    path('Search/', views.Search, name="Search"),
    path('products/<int:myid>', views.prodview, name="productview"),
    path('checkout/', views.checkout, name="checkout"),

]
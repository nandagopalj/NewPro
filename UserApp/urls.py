from django.urls import path
from UserApp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('database/', views.database, name="database"),
    path('products/<catname>', views.products, name="products"),
    path('singleproduct/<int:productid>/', views.singleproduct, name="singleproduct"),
    path('registration/', views.registration, name="registration"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('addcart/', views.addcart, name="addcart"),
    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:cartid>/', views.deletecart, name="deletecart"),
    path('addcheckout/', views.addcheckout, name="addcheckout"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),
]

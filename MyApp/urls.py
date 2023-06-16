from django.urls import path
from MyApp import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:categoryid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:categoryid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:categoryid>/', views.deletecategory, name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:productid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:productid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:productid>/', views.deleteproduct, name="deleteproduct"),
    path('', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:contactid>/', views.deletecontact, name="deletecontact"),
]

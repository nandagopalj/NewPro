from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from MyApp.models import Categorydb, Productdb, Contactdb
from UserApp.models import Userdb, Cartdb, Checkoutdb
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def homepage(req):
    return render(req, "HomePage.html")

def aboutpage(req):
    return render(req, "AboutPage.html")

def contactpage(req):
    return render(req, "ContactPage.html")

def database(req):
    category =Categorydb.objects.all()
    return render(req, "Databases.html", {'category': category})

def products(req, catname):
    category = Categorydb.objects.all()
    product = Productdb.objects.filter(Category_Name=catname)
    return render(req, "Product.html", {'category': category, 'product': product})

def singleproduct(req, productid):
    prosingle= Productdb.objects.get(id=productid)
    return render(req, "SingleProduct.html", {'prosingle': prosingle})

def registration(req):
    return render(req, "Registration.html")

def saveuser(request):
    if  request.method=='POST':
        un = request.POST.get('Username')
        pw = request.POST.get('Password')
        mo = request.POST.get('Mobile')
        em = request.POST.get('Email')
        pi = request.FILES['Profile_Image']
        user = Userdb(Username=un, Password=pw, Mobile=mo, Email=em, Profile_Image=pi)
        user.save()
        messages.success(request, "Login details saved successfully!")
        return redirect(registration)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('Username')
        pw = request.POST.get('Password')
        if Userdb.objects.filter(Username=un, Password=pw).exists():
            request.session['Username'] = un
            request.session['Password'] = pw
            messages.success(request, "Login successful!")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username or Password!")
            return redirect(registration)
    else:
        messages.error(request, "Invalid Username or Password!")
        return redirect(registration)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout successful!")
    return redirect(registration)

def savecontact(request):
    if  request.method=='POST':
        na = request.POST.get('Name')
        mo = request.POST.get('Mobile')
        em = request.POST.get('Email')
        me = request.POST.get('Message')
        contact = Contactdb(Name=na, Mobile=mo, Email=em, Message=me)
        contact.save()
        return redirect(contactpage)

def addcart(request):
    cart = Cartdb.objects.filter(Username=request.session['Username'])
    return render(request, "Cart.html", {'cart':cart})

def savecart(request):
    if  request.method=='POST':
        un = request.POST.get('Username')
        pn = request.POST.get('PName')
        de = request.POST.get('Description')
        qu = request.POST.get('Quantity')
        pr = request.POST.get('TPrice')
        cart = Cartdb(Username=un, Product_Name=pn, Description=de, Quantity=qu, Price=pr)
        cart.save()
        messages.success(request, "Added to cart")
        return redirect(addcart)

def deletecart(request, cartid):
    cart = Cartdb.objects.filter(id=cartid)
    cart.delete()
    messages.success(request, "Item removed from cart")
    return redirect(addcart)

def addcheckout(request):
    return render(request, "Checkout.html")

def savecheckout(request):
    if  request.method=='POST':
        na = request.POST.get('Name')
        co = request.POST.get('Contact')
        ad = request.POST.get('Address')
        pi = request.POST.get('PIN')
        checkout = Checkoutdb(Name=na, Contact=co, Address=ad, PIN=pi)
        checkout.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(homepage)

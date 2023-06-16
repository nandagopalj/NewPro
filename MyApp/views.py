from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from MyApp.models import Categorydb, Productdb, Contactdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def indexpage(req):
    return render(req, "indexpage.html")

def addcategory(req):
    return render(req, "AddCategory.html")

def savecategory(request):
    if  request.method=='POST':
        cn = request.POST.get('Category Name')
        ci = request.FILES['Category Image']
        cd = request.POST.get('Category Description')
        category = Categorydb(Category_Name=cn, Category_Image=ci, Category_Description=cd)
        category.save()
        messages.success(request, "Category saved successfully!")
        return redirect(addcategory)

def displaycategory(req):
    category = Categorydb.objects.all()
    return render(req, "DisplayCategory.html", {'category': category})

def editcategory(req, categoryid):
    category = Categorydb.objects.get(id=categoryid)
    return render(req, "EditCategory.html", {'category': category})

def updatecategory(request, categoryid):
    if  request.method=='POST':
        cn = request.POST.get('Category Name')
        try:
            fs = request.FILES['Category Image']
            fss = FileSystemStorage()
            ci = fss.save(fs.name, fs)
        except MultiValueDictKeyError:
            ci = Categorydb.objects.get(id=categoryid).Category_Image
        cd = request.POST.get('Category Description')
        Categorydb.objects.filter(id=categoryid).update(Category_Name=cn, Category_Image=ci, Category_Description=cd)
        messages.success(request, "Category updated successfully!")
        return redirect(displaycategory)

def deletecategory(request, categoryid):
    category = Categorydb.objects.filter(id=categoryid)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect(displaycategory)

def addproduct(req):
    category = Categorydb.objects.all()
    return render(req, "AddProduct.html", {'category': category})

def saveproduct(request):
    if  request.method=='POST':
        cn = request.POST.get('Category Name')
        pn = request.POST.get('Product Name')
        pp = request.POST.get('Product Price')
        pd = request.POST.get('Product Description')
        pi = request.FILES['Product Image']
        product = Productdb(Category_Name=cn, Product_Name=pn, Product_Price=pp, Product_Description=pd, Product_Image=pi)
        product.save()
        messages.success(request, "Product saved successfully!")
        return redirect(addproduct)

def displayproduct(req):
    product = Productdb.objects.all()
    return render(req, "DisplayProduct.html", {'product': product})

def editproduct(req, productid):
    category = Categorydb.objects.all()
    product = Productdb.objects.get(id=productid)
    return render(req, "EditProduct.html", {'category': category, 'product': product})

def updateproduct(request, productid):
    if  request.method=='POST':
        cn = request.POST.get('Category Name')
        pn = request.POST.get('Product Name')
        pp = request.POST.get('Product Price')
        pd = request.POST.get('Product Description')
        try:
            fs = request.FILES['Product Image']
            fss = FileSystemStorage()
            pi = fss.save(fs.name, fs)
        except MultiValueDictKeyError:
            pi = Productdb.objects.get(id=productid).Product_Image
        Productdb.objects.filter(id=productid).update(Category_Name=cn, Product_Name=pn, Product_Price=pp, Product_Description=pd, Product_Image=pi)
        messages.success(request, "Product updated successfully!")
        return redirect(displayproduct)

def deleteproduct(request, productid):
    product = Productdb.objects.filter(id=productid)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect(displayproduct)

def loginpage(req):
    return render(req, "Loginpage.html")

def adminlogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                request.session['username']=un
                request.session['password']=pw
                messages.success(request, "Login successful!")
                return redirect(indexpage)
            else:
                messages.error(request, "Invalid Username or Password!")
                return redirect(loginpage)
        else:
            messages.error(request, "Invalid Username or Password!")
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successful!")
    return redirect(loginpage)

def displaycontact(req):
    contact = Contactdb.objects.all()
    return render(req, "DisplayContact.html", {'contact': contact})

def deletecontact(request, contactid):
    contact = Contactdb.objects.filter(id=contactid)
    contact.delete()
    messages.success(request, "Message deleted successfully!")
    return redirect(displaycontact)

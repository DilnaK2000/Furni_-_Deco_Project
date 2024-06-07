from django.shortcuts import render,redirect
from LibApp.models import formdb,productdb
from DecoApp.models import contactdb,signupdb,cartdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def home_page(int):
    cat = formdb.objects.all()
    return render(int,"Home.html",{'cat':cat})
def shop_page(sho):
    cat = formdb.objects.all()
    pro=productdb.objects.all()
    return render(sho,"Shop.html" , {'pro':pro , 'cat':cat})
def about_page(ab):
    cat = formdb.objects.all()
    return render(ab,"About.html" ,{'cat':cat})
def contact_page(co):
    cat = formdb.objects.all()
    return render(co,"Contact.html" ,{'cat':cat})
def save_contact(req):
    if req.method=="POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        em = req.POST.get('email')
        me = req.POST.get('mess')
        obj=contactdb(first_name=fn,last_name=ln,email_ad=em,message=me)
        obj.save()
        return redirect(contact_page)
def pro_filter(request,cat_name):
    cat = formdb.objects.all()
    data = productdb.objects.filter(category_name=cat_name)
    return render(request,"Products_filter.html",{'data':data , 'cat':cat})
def single_page(co,pro_id):
    cat = formdb.objects.all()
    data = productdb.objects.get(id=pro_id)
    return render(co,"single_product.html",{'data':data,'cat':cat })
def signup_page(req):
    return render(req,"Signup.html")
def save_signdb(req):
    if req.method=='POST':
        fn = req.POST.get('user')
        em = req.POST.get('mail')
        pd1 = req.POST.get('pass1')
        im = req.FILES['image']
        obj = signupdb(name=fn,email=em,pas1=pd1,img=im)
        if signupdb.objects.filter(name=fn).exists():
            messages.warning(req,"Username already exists...")
            return redirect(signup_page)
        elif signupdb.objects.filter(pas1=pd1).exists():
            messages.warning(req, "Password already exists...")
            return redirect(signup_page)
        else:
            obj.save()
            messages.success(req, "Registered Successfully...")
        return redirect(signup_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('Uname')
        pwd = request.POST.get('Passw')
        if signupdb.objects.filter(name=un,pas1=pwd).exists():
            request.session['name']=un
            request.session['pas1'] = pwd
            messages.success(request, 'Welcome..')
            return redirect(home_page)
        else:
            messages.error(request, 'Invalid Password..')
            return redirect(signup_page)
    else:
        messages.warning(request, 'Invalid UserName..')
        return redirect(signup_page)

def sessionlogout(request):
    del request.session['name']
    del request.session['pas1']
    return redirect(home_page)

def save_cart(req):
    if req.method=="POST":
        un = req.POST.get('username')
        pn = req.POST.get('productname')
        qty = req.POST.get('quantity')
        tp = req.POST.get('totalprice')
        obj = cartdb(username=un,proname=pn,quantity=qty,total=tp)
        obj.save()
        return redirect(home_page)

def cart_page(request):
    data = cartdb.objects.filter(username=request.session['name'])
    total = 0
    for i in data:
        total = total+i.total
    return render(request,"Cart.html",{'data':data , 'total':total})


def delete_page(re,pro_id):
    x = productdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(cart_page)

def user_login_page(request):
    return render(request,"userlogin.html")





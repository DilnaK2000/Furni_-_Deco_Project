from django.shortcuts import render,redirect
from LibApp.models import formdb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from DecoApp.models import contactdb
from django.contrib import messages

# Create your views here.
def index_page(ind):
    return render(ind,"index.html")
def form_page(fo):
    return render(fo,"formelements.html")
def save_page(sav):
    if sav.method=="POST":
        ca = sav.POST.get('cname')
        de = sav.POST.get('desc')
        im = sav.FILES['image']
        obj=formdb(catname=ca,des=de,img=im)
        obj.save()
        messages.success(sav,' Save Successfully...')
        return redirect(form_page)
def display_page(dis):
    data = formdb.objects.all()
    return render(dis,"display.html",{"data":data})
def edit_page(edi,pro_id):
    data = formdb.objects.get(id=pro_id)
    return render(edi,"editform.html",{"data":data})
def update_img(request,pro_id):
    if request.method=="POST":
        ca = request.POST.get('cname')
        de = request.POST.get('desc')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = formdb.objects.get(id=pro_id).img
        formdb.objects.filter(id=pro_id).update(catname=ca,des=de,img=file)
        return redirect(display_page)

def delete_img(request,pro_id):
    x=formdb.objects.filter(id=pro_id)
    x.delete()
    messages.error(request, ' Deleted...')
    return redirect(display_page)
def login_page(log):
    return render(log,"login.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request,x)
                messages.success(request,'Welcome..')
                return redirect(index_page)
            else:
                messages.error(request,'Invalid Username..')
                return redirect(login_page)
        else:
            messages.warning(request, 'Invalid Password..')
            return redirect(login_page)

def product_page(pro):
    data = formdb.objects.all()
    return render(pro,"product.html",{'data':data})

def productsave(dis):
    if dis.method=="POST":
        cn = dis.POST.get('caname')
        pn = dis.POST.get('pname')
        de = dis.POST.get('desc')
        pr = dis.POST.get('prname')
        im = dis.FILES['image']
        obj=productdb(category_name=cn,product_name=pn,Des=de,pri=pr,img=im)
        obj.save()
        messages.success(dis,'Successfully..')
        return redirect(product_page)

def view_prod(req):
    data = productdb.objects.all()
    return render(req,"prodisplay.html", {'data':data})

def proedit_page(req,pro_id):
    cat = productdb.objects.get(id=pro_id)
    pro = formdb.objects.all()
    return render(req,"proedit.html",{'cat':cat , 'pro':pro})

def update_save(request,pro_id):
    if request.method=="POST":
        c = request.POST.get('caname')
        p = request.POST.get('pname')
        d = request.POST.get('desc')
        pr = request.POST.get('prname')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pro_id).img
        productdb.objects.filter(id=pro_id).update(category_name=c,product_name=p,Des=d,pri=pr,img=file)
        return redirect(view_prod)

def delete_page(de,pro_id):
    x = productdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(view_prod)
def cotable(req):
    data = contactdb.objects.all()
    return render(req,"contact_table.html",{'data':data})
def contact_delete(de,pro_id):
    x = contactdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(cotable)

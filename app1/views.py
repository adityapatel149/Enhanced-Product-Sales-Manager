from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Customer,Vendor,Pro
from django.db.models import Q
# Create your views here.

def contact(request):
    if 'vendor' in request.session.keys() or 'cust' in request.session.keys(): #IF SESSION LOGGED IN
        return render(request,"contact.html")   
    else:
        return redirect('login')
def about(request):
    if 'vendor' in request.session.keys() or 'cust' in request.session.keys(): #IF SESSION LOGGED IN
        return render(request,"about.html")   
    else:
        return redirect('login')


def signup_cust(request):
    if request.method=='POST':
        model=Customer()
        model.first=request.POST['fname']
        model.last=request.POST['lname']
        model.email=request.POST['email']
        model.username=request.POST['username']
        model.mobile=request.POST['mobile']
        model.password=request.POST['psw']
        if model.password==request.POST['confirmpass']:
            model.save()
            return redirect('login')
        else:
            return HttpResponse("Password mismatch")
    return render(request, "signup.html")

def signup_vendor(request):
    if request.method=='POST':
        model=Vendor()
        model.cname=request.POST['cname']
        model.email=request.POST['email']
        model.username=request.POST['username']
        model.mobile=request.POST['mobile']
        model.password=request.POST['psw']
        if model.password==request.POST['confirmpass']:
            model.save()
            return redirect('login_vendor')
        else:
            return HttpResponse("Password mismatch")
    return render(request, "signup_vendor.html")

def login(request):
    #a="hello"
    #cal=6+7
    #return render(request, "login.html",{"q":a, "c":cal}) #context, use dictionary
    if request.method=='POST':
        try:
            m=Customer.objects.get(username=request.POST['username'])
            
            if m.password==request.POST['psw']:
                request.session['cust']=m.id # SESSION MANAGEMENT
                return redirect('proall')
            else:
                return HttpResponse("Incorrect Password")
        except:
            return HttpResponse("Incorrect Username")
    return render(request, "login.html")

def login_vendor(request):
    #a="hello"
    #cal=6+7
    #return render(request, "login.html",{"q":a, "c":cal}) #context, use dictionary
    if request.method=='POST':
        try:
            m=Vendor.objects.get(username=request.POST['username'])
            
            if m.password==request.POST['psw']:
                request.session['vendor']=m.id # SESSION MANAGEMENT
                return redirect('proall_vendor')
            else:
                return HttpResponse("Incorrect Password")
        except:
            return HttpResponse("Incorrect Username")
    return render(request, "login_vendor.html")

def logout(request):
    if 'vendor' in request.session.keys(): 
        del request.session['vendor']
        return redirect('login')
    elif 'cust' in request.session.keys():
        del request.session['cust']
        return redirect('login')
    else:
        return redirect('login')


def productview(request,pid):
    if 'cust' in request.session.keys(): #IF SESSION LOGGED IN
        v=Pro.objects.get(id=pid)
        return render(request, "productview.html", {'v':v})    
    else:
        return redirect('login')


def proall(request):    
    if 'cust' in request.session.keys(): #IF SESSION LOGGED IN 
        c=Customer.objects.get(id= int(request.session['cust']))
        a=Pro.objects.all()
        s=search(request)
        return render(request, "proall.html",{'l':a,'s':s,'c':c})
    else:
        return redirect('login')

def proall_vendor(request):    
    if 'vendor' in request.session.keys(): #IF SESSION LOGGED IN 
        v=Vendor.objects.get(id= int(request.session['vendor']))
        products=Pro.objects.filter(vendor=v)
        s=search(request)
        return render(request, "proall_vendor.html",{'l':products,'s':s,'v':v})
    else:
        return redirect('login_vendor')

def search(request):
    q=request.GET.get('search')

    if q:
        pr=Pro.objects.filter(Q(name__icontains=q) | Q(des__icontains=q) | Q(price__icontains=q))
        data={'p':pr}
    else:
        data={}
    #return render(request,'search.html',data)
    return data 


def productadd(request):
    if 'vendor' in request.session.keys(): #IF SESSION LOGGED IN
        if request.method=='POST':
            model = Pro()
            model.name=request.POST['name']
            model.des=request.POST['des']
            model.img=request.FILES.get('image')
            model.price=request.POST['price']
            model.review=request.POST['review']
            model.save()
        return render(request,'productadd.html')
    else:
        return redirect('login_vendor')
    
def productdel(request,pid):
    if 'vendor' in request.session.keys(): #IF SESSION LOGGED IN
        v=Pro.objects.get(id=pid)
        v.delete()
        return redirect("proall_vendor")    
    else:
        return redirect('login_vendor')

    
def productupdate(request,pid):
    if 'vendor' in request.session.keys(): #IF SESSION LOGGED IN
        
        v=Pro.objects.get(id=pid)
        if request.method=='POST':
            v.name=request.POST['name']
            v.des=request.POST['des']
            if request.FILES.get('image') != None:
                v.img=request.FILES.get('image')
            v.price=request.POST['price']
            v.review=request.POST['review']
            v.save()  
            return redirect('proall_vendor')
    else:
        return redirect('login_vendor')
    
    return render(request, "productupdate.html", {'v':v})  

def profilemanager_vendor(request):
    if 'vendor' in request.session.keys():
        v = Vendor.objects.get(id = int(request.session['vendor']))
        if request.POST:
            cname=request.POST['cname']
            email=request.POST['email']
            username=request.POST['username']
            mobile=request.POST['mobile']
            password=request.POST['psw']

            v.cname=cname
            v.email=email
            v.username=username
            v.mobile=mobile
            v.password=password

            v.save()
            return redirect('proall_vendor')
    else:
        return redirect('login_vendor')
    
    return render(request, "profilemanager_vendor.html", {'v':v})



def profilemanager(request):
    if 'cust' in request.session.keys():
        c = Customer.objects.get(id = int(request.session['cust']))
        if request.POST:
            first=request.POST['fname']
            last=request.POST['lname']
            email=request.POST['email']
            username=request.POST['username']
            mobile=request.POST['mobile']
            password=request.POST['psw']

            c.first=first
            c.last=last
            c.email=email
            c.username=username
            c.mobile=mobile
            c.password=password

            c.save()
            return redirect('proall')
    else:
        return redirect('login')
    
    return render(request, "profilemanager.html", {'c':c})

def abc(request):
    a = Vendor.objects.all()  
    b = Vendor.objects.get(id=1) 
    c = Vendor.objects.filter(cname__contains='c') 
    return render(request, "abc.html", {'a':a,'b':b,'c':c})
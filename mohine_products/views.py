from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Products, Orders

def index(request):
    products = Products.objects.all()[:8][::-1]
    if request.user.is_authenticated:
        return render(request,'index_logged_in.html',{'product':products})
    return render(request, 'index.html',{'product':products})

def about(request):
    return render(request, 'about.html')

def thank(request):
    return render(request, 'thank.html')

def view_product(request, id):
    product = Products.objects.filter(id=id).first()
    if request.user.is_authenticated:
        return render(request, 'product_page.html', {"product": product})
    return render(request, 'product_page.html',{'product':product})

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            username=email
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html')
            else:
                user = User.objects.create_user(username,email=email,password=password)
                user.save()
                user.first_name=name
                user.save()
                return redirect('/')
        else:
            return render(request,'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email=request.POST.get('email')
            password=request.POST.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


# Place order or checkout 
def place_order(request):
    if request.method == "POST":
            name=request.POST.get('floating_name', '')
            address=request.POST.get('floating_address', '')
            mobile=request.POST.get('floating_phone', '')
            email=request.POST.get('floating_email', '')
            items_json=request.POST.get('itemsJSON', '')
            print(items_json)

            order=Orders(name=name, email=email, address=address, mobile=mobile, items_json=items_json)
            order.save()
            thanks=True
            id=order.order_id
            return render(request, 'thank.html', {'thanks': thanks, 'id':id})
    else:       
        return render(request,'place_order.html')
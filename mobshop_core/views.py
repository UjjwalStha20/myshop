from django.contrib.auth import login
from django.contrib.auth.decorators  import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from product.models import Product,Category
from .forms import SignUpForm


def landingpage(request):
    products = Product.objects.all()[0:8]
    context = {'products': products}
    return render(request , 'core/frontpage.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('/')
    else :
        form = SignUpForm()

    return render(request,'core/signup.html',{'form' : form})

def signin(request):
    return render(request,'core/signin.html')

def category(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category','')
    if active_category:
        products = products.filter(category__name = active_category)

    query = request.GET.get('search_query','')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query)| Q(category__name__icontains=query))

    context = { 
        'products': products,
        'categories' :categories,
        'active_category': active_category,
    }
    return render(request,'core/categorypage.html',context)

@login_required
def myaccount(request):
    return render(request,'core/myaccount.html')

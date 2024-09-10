from django.contrib.auth import views
from django.urls import path

from mobshop_core.views import landingpage, category, signup, myaccount
from product.views import product

urlpatterns =[
    path('',landingpage,name='landingpage'),
    path('signup/',signup,name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signin/',views.LoginView.as_view(template_name='core/signin.html'),name='signin'),
    path('category/',category,name='category'),
    path('category/<int:id>/',product,name='product'),
    path('account/', myaccount,name='myaccount')
]
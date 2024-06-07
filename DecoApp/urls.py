from django.urls import path
from DecoApp import views

urlpatterns  = [
    path('',views.home_page,name="Home"),
    path('Shop/',views.shop_page,name="Shop"),
    path('About/',views.about_page,name="About"),
    path('Contact',views.contact_page,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('pro_filter/<cat_name>/',views.pro_filter,name="pro_filter"),
    path('single_page/<int:pro_id>/',views.single_page,name="single_page"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('save_signdb/',views.save_signdb,name="save_signdb"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('sessionlogout/',views.sessionlogout,name="sessionlogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_page/<int:pro_id>/',views.delete_page,name="delete_page"),
    path('user_login_page/',views.user_login_page,name="user_login_page")

]
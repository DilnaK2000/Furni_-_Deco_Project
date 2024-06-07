from django.urls import path
from LibApp import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('form_page/',views.form_page,name="form_page"),
    path('save_page/',views.save_page,name="save_page"),
    path('display_page/',views.display_page,name="display_page"),
    path('edit_page/<int:pro_id>/',views.edit_page,name="edit_page"),
    path('update_img/<int:pro_id>/',views.update_img,name="update_img"),
    path('delete_img/<int:pro_id>/',views.delete_img,name="delete_img"),
    path('login_page/',views.login_page,name="login_page"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('product_page/',views.product_page,name="product_page"),
    path('productsave/',views.productsave,name="productsave"),
    path('view_prod/',views.view_prod,name="view_prod"),
    path('proedit_page/<int:pro_id>/',views.proedit_page,name="proedit_page"),
    path('update_save/<int:pro_id>/',views.update_save,name="update_save"),
    path('delete_page/<int:pro_id>/',views.delete_page,name="delete_page"),
    path('cotable/',views.cotable,name="cotable"),
    path('contact_delete/<int:pro_id>/',views.contact_delete,name="contact_delete")
]
from django.urls import path,re_path,include
from  . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name = "logout"),

    path('account/',views.accountSettings, name="account"),
    path('', views.home,name="home"), 
    path('user/', views.userPage, name = "user-page"),
    path('products/', views.products,name="products"),
    path('customer/<str:pk_test>/', views.customer,name="customer"),
    
    path('create_order/<str:pk>',views.createOrder, name = "create_order"),
    path('update_order/<str:pk>/',views.updateOrder, name = "update_order"),
    path('delete_order/<str:pk>/',views.deleteOrder, name = "delete_order"),

    # password reset

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
        name="reset_password"),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),
    
    #path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
    #    auth_views.PasswordResetConfirmView.as_view(), 
    #    name='password_reset_confirm'),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
        name='password_reset_confirm'),
    

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),


]

"""
1. submit email form            //PasswordResetView.as_view()

2. email sent success message   //PasswordResetDoneView.as_view()

3. link to password Reset       //PasswordResetConfirmView.as_view() 
   form in email

4. password successfully        //PasswordresetCompleteView.as_view()
   changed message
"""
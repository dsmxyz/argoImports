from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customers/', views.customers, name="customers"),
    path('customers/<int:pk>', views.customerInfo, name="customerInfo"),
    path('deleteCustomers/<int:pk>', views.deleteCustomers, name='deleteCustomers'),
    path('addCustomers/', views.addCustomers, name="addCustomers"),
    path('updateCustomers/<int:pk>', views.updateCustomers, name="updateCustomers"),
    path('trucks/', views.trucks, name="trucks"),
    path('trucks/<int:pk>', views.truckInfo, name="truckInfo")
         

    
]

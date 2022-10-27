from django.urls import path
from .views import ClientView

urlpatterns = [
    path('client/', ClientView.as_view(), name='clients_list')
    #path('employee/', EmployeeView.as_view(), name='employees_list')
]
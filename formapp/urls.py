from django.urls import path,include
from .import views


urlpatterns = [
    path('add',views.add,name='add'),
    path('addemp',views.addemp,name='addemp'),
    path('show_employees',views.show_employees,name='show_employees'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('sendmail',views.sendmail,name='sendmail'),
]
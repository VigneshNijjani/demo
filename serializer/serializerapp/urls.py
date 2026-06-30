from django.urls import path
from . import views

app_name='serializerapp'

urlpatterns=[
    path("",views.create_employee),
    path('view/<int:inp_id>',views.view_employee),
    path('update/<int:inp_id>',views.update_employee),
]
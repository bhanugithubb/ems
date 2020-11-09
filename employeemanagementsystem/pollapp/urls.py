from django.urls import path
from pollapp import views

urlpatterns=[
    path('',views.index,name="polls_list"),
    path('<int:id>/details/',views.detail),
    path('<int:id>/', views.poll),

]
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('food/<int:id>',views.detail,name='detail'),
    path('update/<int:item_id>', views.update, name='update'),
    path('delete/<int:food_id>', views.delete, name='delete'),

    path('add/', views.add_product, name='add_product')

]
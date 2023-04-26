from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('<int:menu_id>/like',views.like, name='like'),
    path('<int:menu_id>/delete', views.delete, name="delete"),
    path('<int:menu_id>/edit', views.edit, name="edit"),
    path('map', views.map, name='map'),
]
from django.urls import path
from . import views     # Djangoのpath関数と、blogアプリの全てのビューをインポートする

urlpatterns = [
    path('', views.number, name='number'), #'http://127.0.0.1:8000/' にアクセスしたら、numberにつなげる。
    path('base/', views.post_list,name='post_list'),
    path('exit/', views.exit ,name='exit'),
    path('transfer/', views.transfer,name='transfer'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

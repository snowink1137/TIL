from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    # Read
    path('', views.article_list, name='article_list'),  # DOMAIN/articles/
    path('<int:id>/', views.article_detail, name='article_detail'),  # DOMAIN/articles/1/

]

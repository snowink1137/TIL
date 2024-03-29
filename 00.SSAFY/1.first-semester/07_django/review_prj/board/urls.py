from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), #DOMAIN/board_ad/index
    path('greeting/<str:name>/<str:role>/', views.greeting), #DOMAIN/board_ad/greeting/john
    # Create
    # /articles/new => html (all articles)
    path('articles/new/', views.article_new),
    # /articles/create/1 => html (article with id 1)
    path('articles/create/', views.article_create),
    # Read
    # /articles => html (all articles)
    path('articles/', views.article_list),
    # /articles/1 => (article with id 1)
    path('articles/<int:id>/', views.article_detail),
    # Update
    # /articles/1/edit => html (article id=1 수정하는 화면)
    path('articles/<int:id>/edit/', views.article_edit),
    # /articles/1/update => DB update article id=1
    path('articles/<int:id>/update/',  views.article_update),

    # Delete
    # /articles/1/delete => DB delete article id=1
    path('articles/<int:id>/delete/',  views.article_delete),
]

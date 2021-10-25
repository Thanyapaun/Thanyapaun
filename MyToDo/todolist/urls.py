from django.urls import path
from .views import home, todo, todoDetail
# from todo import views


urlpatterns = [
    path('', home),
    path('home/', home),
    path('todo/', todo),
    path('todo/<int:id>', todoDetail)
    # path('', views.index, name='index'),
    # path('submit', views.submit, name='index')
]

from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
        path('', views.book_list, name='list'),
        path('add/book', views.add_book, name='add'),
        path('book/<int:pk>', views.book_detail, name='detail'),
        path('book/update/<int:pk>', views.update_book, name='update'),
        path('book/delete/<int:pk>', views.delete_book, name='delete'),
        path('logout/', views.logout_view, name='logout')
]
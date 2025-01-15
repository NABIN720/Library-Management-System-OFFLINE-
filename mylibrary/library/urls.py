# from django.contrib import admin
from django.urls import path
# from django.contrib import 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('view_students',views.view_students,name="Students"),
    path('add_student',views.add_student,name="add_student"),
    path('add_book',views.add_book,name="add_book"),
    path('view_books',views.view_books,name="Book"),
    path('add_issue', views.add_book_issue,name='add_issue'),
    path('book_issued',views.book_issued,name="Books Issued"),
    path('dashboard/<int:pk>/',views.dashboard,name='dashboard' ),
    path('dashboard/<int:pk>/return/',views.return_book,name='return_book' ),
        
]

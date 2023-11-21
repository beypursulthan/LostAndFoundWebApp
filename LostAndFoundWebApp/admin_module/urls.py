from .views import register
from .views import register, user_login
from django.contrib.auth import views as auth_views
from .views import lost_items, found_items, post_lost_item, edit_lost_item, delete_lost_item, mark_item_found
from .views import lost_items, found_items, post_lost_item, edit_lost_item, delete_lost_item
from .views import lost_items, found_items, post_lost_item
from django.urls import path
from .views import lost_items, found_items

urlpatterns = [
    path('lost/', lost_items, name='lost_items'),
    path('found/', found_items, name='found_items'),
]


urlpatterns = [
    path('lost/', lost_items, name='lost_items'),
    path('found/', found_items, name='found_items'),
    path('post_lost/', post_lost_item, name='post_lost_item'),
]


urlpatterns = [
    path('lost/', lost_items, name='lost_items'),
    path('found/', found_items, name='found_items'),
    path('post_lost/', post_lost_item, name='post_lost_item'),
    path('edit_lost/<int:item_id>/', edit_lost_item, name='edit_lost_item'),
    path('delete_lost/<int:item_id>/', delete_lost_item, name='delete_lost_item'),
]


urlpatterns = [
    path('lost/', lost_items, name='lost_items'),
    path('found/', found_items, name='found_items'),
    path('post_lost/', post_lost_item, name='post_lost_item'),
    path('edit_lost/<int:item_id>/', edit_lost_item, name='edit_lost_item'),
    path('delete_lost/<int:item_id>/', delete_lost_item, name='delete_lost_item'),
    path('mark_found/<int:item_id>/', mark_item_found, name='mark_item_found'),
]


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

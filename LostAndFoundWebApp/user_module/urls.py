from django.contrib.auth import views as auth_views
from .views import register, user_login
from .views import register
from .views import user_lost_items, user_found_items, post_user_lost_item, edit_user_lost_item, delete_user_lost_item, mark_user_item_found
from .views import user_lost_items, user_found_items, post_user_lost_item, edit_user_lost_item, delete_user_lost_item
from .views import user_lost_items, user_found_items, post_user_lost_item
from django.urls import path
from .views import user_lost_items, user_found_items

urlpatterns = [
    path('user_lost/', user_lost_items, name='user_lost_items'),
    path('user_found/', user_found_items, name='user_found_items'),
]


urlpatterns = [
    path('user_lost/', user_lost_items, name='user_lost_items'),
    path('user_found/', user_found_items, name='user_found_items'),
    path('post_user_lost/', post_user_lost_item, name='post_user_lost_item'),
]


urlpatterns = [
    path('user_lost/', user_lost_items, name='user_lost_items'),
    path('user_found/', user_found_items, name='user_found_items'),
    path('post_user_lost/', post_user_lost_item, name='post_user_lost_item'),
    path('edit_user_lost/<int:item_id>/',
         edit_user_lost_item, name='edit_user_lost_item'),
    path('delete_user_lost/<int:item_id>/',
         delete_user_lost_item, name='delete_user_lost_item'),
]


urlpatterns = [
    path('user_lost/', user_lost_items, name='user_lost_items'),
    path('user_found/', user_found_items, name='user_found_items'),
    path('post_user_lost/', post_user_lost_item, name='post_user_lost_item'),
    path('edit_user_lost/<int:item_id>/',
         edit_user_lost_item, name='edit_user_lost_item'),
    path('delete_user_lost/<int:item_id>/',
         delete_user_lost_item, name='delete_user_lost_item'),
    path('mark_user_found/<int:item_id>/',
         mark_user_item_found, name='mark_user_item_found'),
]


urlpatterns = [
    # ...
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

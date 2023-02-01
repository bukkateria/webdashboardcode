from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path("", DashboardLogin.as_view(), name="login"),
    path("home/", home, name="home"),
    
    path("posts/menus/", menus, name="menus"),
    path("posts/delete-menu/", delete_menu, name="delete_menu"),
    
    path("posts/recipes/", recipes, name="recipes"),
    path("posts/delete-reipe/", delete_recipe, name="delete_recipe"),
    
    path("posts/explore/", explore, name="explore"),
    path("posts/delete-explore/", delete_explore, name="delete_explore"),
    
    path("users/", users, name="users"),
    path("delete-user/", delete_user, name="delete_user"),
    
    path("orders/", orders, name="orders"),
    path("delete-order/", delete_order, name="delete_order"),
    
    path("blocked-requests/", blocked_requests, name="blocked_requests"),
    path("delete-blocked-request/", delete_blocked_request, name="delete_blocked_request"),
    
    path("manage-ads/", ads, name="ads"),
    path("create-ad/", create_ad, name="create_ad"),
    path("delete-ad/", delete_ad, name="delete_ad"),
    
    path("notifications/", notifications, name="notifications"),
    path("delete-notification/", delete_notification, name="delete_notification"),
]

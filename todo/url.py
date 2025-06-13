from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login_view,name='login'),
    path('signup',views.register,name='signup'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('logout', views.logout_view,name='logout'),
    path('update/<int:todo_id>', views.update, name='update'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
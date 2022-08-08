from django.urls import re_path
from django.contrib import admin
from django.urls import path

from task.views import GenerateRandomUserView, UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('users/', UsersListView.as_view(), name='users_list'),
    re_path('generate/', GenerateRandomUserView.as_view(), name='generate')

]
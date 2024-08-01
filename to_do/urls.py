from django.contrib import admin
from django.urls import path
from to_do_list.views import *


urlpatterns = [
    path('todo/', todo ,name='todo'),
    path('delete_todo/<id>/', delete_todo ,name='delete_todo'),

    path('admin/', admin.site.urls),
]

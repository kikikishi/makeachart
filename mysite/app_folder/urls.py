from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    path('index/', views.index, name='index'),
    # 以下を追記(views.pyのcall_write_data()にデータを送信できるようにする)
    path("ajax/", views.call_write_data, name="call_write_data"),
]

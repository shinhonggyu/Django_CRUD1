from django.urls import path, re_path
from . import views

app_name = 'instagram'  # URL Reverse에서 namespace 역할

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
    re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
]

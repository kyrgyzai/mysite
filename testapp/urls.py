from django.urls import path
from . import views 

app_name = 'testapp'
urlpatterns = [
    path('<int:question_id>/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('info/', views.info, name='info'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name="news_list"),
    path('detail/<str:pk>/', views.news_detail, name="news_detail"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.create_user, name="register"),
    path('create/', views.create_new_post, name="create"),
    path('categories/international/', views.international_page, name="international"),
    path('categories/fashion/', views.fashion_page, name="fashion"),
    path('categories/agriculture/', views.agriculture_page, name="agriculture"),
    path('categories/finance/', views.finance_page, name="finance"),
    path('categories/health/', views.health_page, name="health"),
    path('categories/local/', views.local_page, name="local"),
    path('categories/oil/', views.oil_page, name="oil"),
    path('categories/politics/', views.politics_page, name="politics"),
    path('categories/sports/', views.sports_page, name="sports"),
    path('categories/tech/', views.tech_page, name="tech"),
    path('categories/weather/', views.weather_page, name="weather")
]


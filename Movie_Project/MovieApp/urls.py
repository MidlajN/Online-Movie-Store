from django.conf.urls.static import static
from django.urls import path

from MovieApp import views
from Movie_Project import settings

app_name = 'MovieApp'
urlpatterns = [
    path('', views.product, name='product'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



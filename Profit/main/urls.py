from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(300)(views.MainPage.as_view()), name='main'),
    path('view_data/', views.ViewData.as_view(), name='view_data')
]
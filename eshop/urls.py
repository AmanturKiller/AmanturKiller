"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import homepage, product_detail, user_cabinet, users_list
from costumerapp.views import costumer_view
from news.views import news_list, new_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('user/<int:id>/', user_cabinet, name='user-cabinet'), 
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('costumers/', costumer_view),
    path('news/', news_list, name='news-list'),
    # /new-detail/8/
    path('new-detail/<int:id>/', new_detail, name='new-detail'),
    path('users/', users_list),
]

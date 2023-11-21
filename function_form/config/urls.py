"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from app.views import hub_page, Hey_You, Age_in_2050, Order
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hub_page, name="hub"),
    path("hey/", Hey_You, name="HEY"),
    path("age_in_2050/", Age_in_2050, name="AGE"),
    path("order/", Order, name="ORDER"),
]

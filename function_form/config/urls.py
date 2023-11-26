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


from app.views import hub_page, Open_Page, Hey_You, Age_in_2050, Order, Codingbat_Hub, font_times, teen, xyz, centered_average

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Open_Page, name="home"),
    path("codinghub/", Codingbat_Hub, name="CBHub"),
    path("codinghub/warmup-2/font-times/", font_times, name="FONT"),
    path("codinghub/logic-2/no-teen-sum/", teen, name="TEEN"),
    path("codinghub/string-2/xyz-there", xyz, name="XYZ"),
    path("codinghub/list-2/centered-average", centered_average, name="AVERAGE"),
    path("functionhub/", hub_page, name="hub"),
    path("functionhub/hey/", Hey_You, name="HEY"),
    path("functionhub/age_in_2050/", Age_in_2050, name="AGE"),
    path("functionhub/order/", Order, name="ORDER"),
]

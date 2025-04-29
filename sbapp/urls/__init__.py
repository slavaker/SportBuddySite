
from django.urls import path, include
from sbapp.views import home

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", home)
]
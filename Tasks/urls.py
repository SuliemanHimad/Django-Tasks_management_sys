
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # Authentication
    path("", include("task_mng.urls")),  # Tasks
]

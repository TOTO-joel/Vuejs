# from app import views
# from django.conf import settings
# from django.conf.urls import url
# from django.conf.urls.static import static

# urlpatterns=[
#     url(r'^department$',views.departmentApi),
#     url(r'^department/([0-9]+)$',views.departmentApi),

#     url(r'^employee$',views.employeeApi),
#     url(r'^employee/([0-9]+)$',views.employeeApi),

#     url(r'^employee/savefile',views.SaveFile)
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.urls import path, re_path  # Import the correct functions
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('department', views.departmentApi),  # Use 'path()' for simple URLs
    re_path(r'^department/([0-9]+)$', views.departmentApi),  # Use 're_path()' for regex
    path('employee', views.employeeApi),  # Use 'path()' for simple URLs
    re_path(r'^employee/([0-9]+)$', views.employeeApi),  # Use 're_path()' for regex
    path('employee/savefile', views.SaveFile),  # Use 'path()' for simple URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

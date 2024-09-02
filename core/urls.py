from django.urls import path
from .views import (
    DepartmentListCreateView, DepartmentDetailView,
    DoctorListCreateView, DoctorDetailView,
    PatientListCreateView, PatientDetailView,
    PatientRecordListCreateView, PatientRecordDetailView
)

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient_records/', PatientRecordListCreateView.as_view(), name='patientrecord-list-create'),
    path('patient_records/<int:pk>/', PatientRecordDetailView.as_view(), name='patientrecord-detail'),
]

# Include these URLs in your main project URLs (healthapi/urls.py)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

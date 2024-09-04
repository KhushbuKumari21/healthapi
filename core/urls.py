from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient-records/', views.PatientRecordListCreateView.as_view(), name='patient-record-list-create'),
    path('patient-records/<int:pk>/', views.PatientRecordDetailView.as_view(), name='patient-record-detail'),
    path('department/<int:pk>/doctors/', views.department_doctors, name='department-doctors'),
    path('department/<int:pk>/patients/', views.department_patients, name='department-patients'),
    path('register/', views.register, name='register'),
]

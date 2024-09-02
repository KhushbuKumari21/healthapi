from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Department, Patient, Doctor, PatientRecord
from .serializers import DepartmentSerializer, PatientSerializer, DoctorSerializer, PatientRecordSerializer

# Custom Permissions
class IsDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class IsPatient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsDoctor]

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsPatient]

class PatientRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return PatientRecord.objects.all()
        patient = Patient.objects.filter(user=user).first()
        if patient:
            return PatientRecord.objects.filter(department=patient.department)
        return PatientRecord.objects.none()

class PatientRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return PatientRecord.objects.all()
        patient = Patient.objects.filter(user=user).first()
        if patient:
            return PatientRecord.objects.filter(patient=patient)
        return PatientRecord.objects.none()

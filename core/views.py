from django.http import HttpResponse
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Department, Patient, Doctor, PatientRecord
from core.serializers import DepartmentSerializer, PatientSerializer, DoctorSerializer, PatientRecordSerializer, UserSerializer
from core.permissions import IsDoctor, IsPatient
from django.shortcuts import render


# View to render the Home page
def home(request):
    return render(request, 'home.html')

# View to render the About page
def about(request):
    return render(request, 'about.html')

# API Views
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
        if user.is_staff:  # For doctors
            return PatientRecord.objects.filter(doctor__user=user)
        patient = Patient.objects.filter(user=user).first()  # For patients
        if patient:
            return PatientRecord.objects.filter(patient=patient)
        return PatientRecord.objects.none()

class PatientRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # For doctors
            return PatientRecord.objects.filter(doctor__user=user)
        patient = Patient.objects.filter(user=user).first()  # For patients
        if patient:
            return PatientRecord.objects.filter(patient=patient)
        return PatientRecord.objects.none()

@api_view(['GET'])
def department_doctors(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'detail': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        doctors = Doctor.objects.filter(department=department)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def department_patients(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'detail': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        patients = Patient.objects.filter(department=department)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
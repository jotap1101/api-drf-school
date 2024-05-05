from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from school.models import Course, Enrollment, Student
from school.serializers import CourseSerializer, CourseEnrollmentSerializer, EnrollmentSerializer, StudentSerializer, StudentEnrollmentSerializer

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing enrollment instances.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentEnrollmentViewSet(generics.ListAPIView):
    """
    A viewset for viewing and editing enrollment instances.
    """
    serializer_class = StudentEnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student_id=self.kwargs['pk'])
    
class CourseEnrollmentViewSet(generics.ListAPIView):
    """
    A viewset for viewing and editing enrollment instances.
    """
    serializer_class = CourseEnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(course_id=self.kwargs['pk'])
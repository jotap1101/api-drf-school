from rest_framework import serializers
from school.models import Course, Enrollment, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

# Crie uma classe para listar as matrículas de um aluno
class StudentEnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')
    status = serializers.SerializerMethodField()
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = '__all__'

    def get_status(self, obj):
        return obj.get_status_display()

    def get_period(self, obj):
        return obj.get_period_display()
        
class CourseEnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')
    status = serializers.SerializerMethodField()
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = '__all__'

    def get_status(self, obj):
        return obj.get_status_display()

    def get_period(self, obj):
        return obj.get_period_display()
from django.contrib import admin
from school.models import Course, Enrollment, Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['code', 'name', 'level', 'description', 'created_at', 'updated_at']
    list_display_links = ['code', 'name']
    list_filter = ['level', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['code', 'name', 'level']

class StudentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['name', 'rg', 'cpf', 'birth_date', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['name', 'rg', 'cpf']

class EnrollmentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['student', 'course', 'status', 'period', 'created_at', 'updated_at']
    list_display_links = ['student', 'course']
    list_filter = ['status', 'period', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['student', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
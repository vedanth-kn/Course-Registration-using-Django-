from django.contrib import admin
from Home.models import Contact, Student, Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Course)
# admin.site.register(Enrollment)
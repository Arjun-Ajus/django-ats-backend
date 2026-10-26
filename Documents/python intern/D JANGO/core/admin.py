from django.contrib import admin
from .models import JobUser, Job, Application

# Register your models here.
admin.site.register(JobUser)
admin.site.register(Job)
admin.site.register(Application)
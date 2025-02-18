from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'facility_name', 'bill_rate', 'pay_rate', 'city', 'state', 'country', 'job_type', 'start_date', 'end_date', 'recruiter', 'publish', 'created_time')
    list_filter = ('job_type', 'state', 'country', 'publish', 'created_time')
    search_fields = ('job_title', 'facility_name', 'recruiter', 'reference_number')
    ordering = ('-created_time',)

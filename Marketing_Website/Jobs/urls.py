from django.urls import path
from .views import Homepage, Extract_Data_From_XML, ShowJobs, job_detail

urlpatterns = [
    path('', Homepage, name='Homepage'),  # Example view
    path('fetch_jobs_from_xml/', Extract_Data_From_XML, name="Extract_Data_From_XML"),
    path('jobs/', ShowJobs, name="ShowJobs"),
    path('job/<str:job_title_id>/', job_detail, name='job_detail'),
]

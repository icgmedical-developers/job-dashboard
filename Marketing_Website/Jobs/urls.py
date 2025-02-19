from django.urls import path
from .views import Homepage, Extract_Data_From_XML, job_detail, ShowJob_Category

urlpatterns = [
    path('', Homepage, name='Homepage'),  # Example view
    path('fetch_jobs_from_xml/', Extract_Data_From_XML, name="Extract_Data_From_XML"),
    path('job/<str:job_title_id>/', job_detail, name='job_detail'),
    path('show-jobs/<str:job_types>/', ShowJob_Category, name='ShowJob_Category'),
]

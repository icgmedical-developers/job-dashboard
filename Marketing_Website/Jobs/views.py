from django.http import JsonResponse
import requests, re
import xml.etree.ElementTree as ET
from .models import Job
from datetime import datetime
from django.http import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def format_date(date_str):
    """Convert date from DD/MM/YYYY to YYYY-MM-DD format."""
    if date_str:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format: {date_str}")  # Debugging
            return None  # Return None if the format is incorrect
    return None  # Handle empty values

def extract_values(html):
    # Regular expression to match the href value and the title between the anchor tags
    match = re.search(r'<a href="/([^"]+)"[^>]*>(.*?)</a>', html)
    
    if match:
        # Extract the values
        href_value = match.group(1)  # No leading '/' in the href_value now
        title = match.group(2)
        return href_value, title
    else:
        return None, None

def Homepage(request):
    recent_jobs = Job.objects.all().order_by('-post_date')[:8]  # Fetch latest 8 jobs
    print(recent_jobs)
    return render(request,'jobs/index.html', {'recent_jobs':recent_jobs})

def get_text(element):
    """Extract text from an XML element, return an empty string if None."""
    return element.text.strip() if element is not None and element.text else ""

def Extract_Data_From_XML(request):
    # Base URL
    base_url = "https://icgmedical.my.salesforce-sites.com/apex/XMLFeedPage?page="

    # Fetch the first page to get the total number of pages
    response = requests.get(base_url + "1")

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        
        # Get the total number of pages
        total_pages_element = root.find("PageNumbers")
        total_pages = int(get_text(total_pages_element)) if total_pages_element is not None else 1

        print(f"Total Pages Found: {total_pages}")

        jobs = []

        # Iterate through all pages
        for page in range(1, total_pages + 1):
            print(f"Fetching page {page}/{total_pages}...")

            # Fetch the page content
            response = requests.get(base_url + str(page))

            if response.status_code == 200:
                root = ET.fromstring(response.content)

                for job in root.findall("job"):
                    # Extract reference number
                    reference_number = job.find("referencenumber")
                    
                    if reference_number is not None and reference_number.text:
                        reference_number = reference_number.text.strip()  # Get the actual text value

                    # Check if a job with this reference_number already exists
                    if Job.objects.filter(reference_number=reference_number).exists():
                        print(f"Skipping duplicate job with reference number: {reference_number}")
                        continue  # Skip this job

                    # Extract other job details
                    job_data = {
                        "job_title_id": extract_values(get_text(job.find("title")))[0],
                        "job_title": extract_values(get_text(job.find("title")))[1],
                        "facility_name": get_text(job.find("FacilityName")),
                        "bill_rate": get_text(job.find("BillRate")),
                        "pay_rate": get_text(job.find("PayRate")),
                        "source_name": get_text(job.find("SourceName")),
                        "unit_description": get_text(job.find("UnitDescription")),
                        "city": get_text(job.find("city")),
                        "state": get_text(job.find("state")),
                        "country": get_text(job.find("country")),
                        "job_type": get_text(job.find("jobType")),
                        "start_date": format_date(get_text(job.find("startdate"))),
                        "end_date": format_date(get_text(job.find("enddate"))),
                        "job_description": get_text(job.find("job_description")),
                        "job_url": get_text(job.find("url")),
                        "recruiter": get_text(job.find("recruiter")),
                        "recruiter_email": get_text(job.find("recruiter-email")),
                        "hot_job": get_text(job.find("HotJob")).strip().lower() in ["true", "1"],  
                        "reference_number": reference_number,  # Already extracted above
                        "specialty": get_text(job.find("specialty")),
                        "business_type": get_text(job.find("businessType")),
                        "zipcode": get_text(job.find("zipcode")),
                        "positions": int(get_text(job.find("positions")) or 0),  
                        "employer": get_text(job.find("employer")),
                        "discipline": get_text(job.find("Discipline")),
                        "category": get_text(job.find("category")),
                        "experience": get_text(job.find("experience")),
                        "description": get_text(job.find("description")),
                        "default_email": get_text(job.find("default_email")),
                        "post_date": format_date(get_text(job.find("postdate"))),
                        "duration": get_text(job.find("duration")),
                        "shift": get_text(job.find("shift")),
                        "job_robotix_type": get_text(job.find("jobRobotix_jobType")),
                        "vms_job_type": get_text(job.find("vms_jobType")),
                        "created_time": datetime.now(),
                        "publish": False,  
                    }

                    # Save the job entry
                    Job.objects.create(**job_data)
                    print(f"Added job: {reference_number}")
            else:
                print(f"Failed to fetch page {page}. Skipping...")

        print("Job listings have been successfully added to the database.")
        return JsonResponse({"status": "success", "message": "Job listings have been successfully added."})

    else:
        print(f"Failed to fetch XML. Status Code: {response.status_code}")
        return JsonResponse({"status": "failure", "message": f"Failed to fetch XML. Status Code: {response.status_code}"})


def ShowJobs(request):
    all_jobs = Job.objects.all().order_by('post_date')  # Order jobs by 'created_at' or another field
    
    paginator = Paginator(all_jobs, 18)  # Show 18 jobs per page
    
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the jobs for the current page

    print(page_obj.object_list)  # Check the jobs on the current page

    return render(request, 'jobs/view_jobs.html', {'page_obj': page_obj})

def job_detail(request, job_title_id):
    job = get_object_or_404(Job, job_title_id=job_title_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

        

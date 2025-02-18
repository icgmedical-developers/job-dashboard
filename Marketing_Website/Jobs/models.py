from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_title_id= models.CharField(max_length=20)
    slug = models.SlugField(max_length=255,unique=True, blank=True, null=True)  # Auto-generated slug
    facility_name = models.CharField(max_length=255)
    bill_rate = models.CharField(max_length=50, blank=True, null=True)
    pay_rate = models.CharField(max_length=50, blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    unit_description = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_url = models.URLField(blank=True, null=True)
    recruiter = models.CharField(max_length=255, blank=True, null=True)
    recruiter_email = models.EmailField(blank=True, null=True)
    hot_job = models.BooleanField(default=False)
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    positions = models.PositiveIntegerField(blank=True, null=True)
    employer = models.CharField(max_length=255, blank=True, null=True)
    discipline = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    default_email = models.EmailField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    shift = models.CharField(max_length=100, blank=True, null=True)
    job_robotix_type = models.CharField(max_length=100, blank=True, null=True)
    vms_job_type = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_title} ({self.job_title_id})"

    def save(self, *args, **kwargs):
        """Auto-generate a unique slug from job title and job title ID."""
        if not self.slug:
            base_slug = slugify(f"{self.job_title}-{self.job_title_id}")
            slug = base_slug
            count = 1
            
            while Job.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug

        super().save(*args, **kwargs)

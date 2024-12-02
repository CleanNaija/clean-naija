from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.gis.db import models as gis_models 
#from osm_field.models import PointField  # Correct import for PointField we can use osm_fields later for easier integration 


class CustomUser(AbstractUser):
    ROLE_CHOICES=[
        ('admin', 'Admin'),
        ('collector', 'Waste Collector'),
        ('user', 'Regular User'),
    ]
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    



class WasteBin(models.Model):
    address = gis_models.CharField(max_length=255)
    location = gis_models.PointField()  # Store lat/long as a point
    bin_type = gis_models.CharField(max_length=100, choices=[('recyclable', 'Recyclable'), ('general', 'General'), ('organic', 'Organic')])
    status = models.CharField(max_length=50, choices=[('full', 'Full'), ('empty', 'Empty')])
    capacity = models.FloatField(default=0)  # Capacity in liters
    def __str__(self):
        return f'{self.address} - {self.bin_type}'
    

class WasteCollectionRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    collection_date = models.DateField()
    location = gis_models.PointField()  # Store lat/long of the request
    waste_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    priority = models.CharField(max_length=20, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium')

    def __str__(self):
        return f'Request for {self.waste_type} at {self.address}'

    class Meta:
        ordering = ['collection_date']


class WasteType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='waste_icons/', null=True, blank=True)  # Optional icon for waste type
    is_active = models.BooleanField(default=True)  # To deactivate waste types no longer in use
    def __str__(self):
        return self.name

class CollectionPoint(models.Model):
    name=models.CharField(max_length=100)
    location=gis_models.PointField() #Requires PostGIS
    address=models.TextField(blank=True,null=True)
    description = models.TextField()
    collection_date = models.DateTimeField()
    capacity = models.FloatField(default=0)  # Capacity in liters
    contact_info = models.CharField(max_length=255, blank=True, null=True)  # Contact information for support
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    operating_hours = models.CharField(max_length=255, blank=True, null=True)  # Time slots for collection

    def __str__(self):
        return self.name
    
    
class CollectionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests')
    waste_type = models.ForeignKey(WasteType, on_delete=models.CASCADE)
    collection_point = models.ForeignKey(CollectionPoint, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)  # Tracks when the collection request was completed

    def __str__(self):
        return f"Request by {self.user.username} ({self.status})"


class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('missed_collection', 'Missed Collection'),
        ('illegal_dumping', 'Illegal Dumping'),
        ('general', 'General Issue'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('resolved', 'Resolved'), ('unresolved', 'Unresolved')], default='unresolved')
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_reports')


    def __str__(self):
        return f"Report by {self.user.username} ({self.report_type})"


class WasteAnalytics(models.Model):
    waste_type = models.ForeignKey(WasteType, on_delete=models.CASCADE)
    total_collected = models.FloatField(default=0)  # Amount in kg or other units
    total_requests = models.IntegerField(default=0)
    average_collected_per_day = models.FloatField(default=0)  # Average collection per day (kg/day)
    average_waste_per_collection = models.FloatField(default=0)  # Average waste per collection (kg)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Analytics for {self.waste_type.name}"
    




from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin  # Correct import for geospatial models
from .models import CustomUser, WasteBin, WasteCollectionRequest, WasteType, CollectionPoint, CollectionRequest, Report, WasteAnalytics
from django.contrib.auth.admin import UserAdmin

# Register CustomUser with custom fields
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_verified', 'is_staff', 'is_active']
    list_filter = ['role', 'is_verified', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'is_verified', 'phone_number', 'address')}),  
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'is_verified', 'phone_number', 'address')}),  
    )

# WasteBin Admin Setup
class WasteBinAdmin(GISModelAdmin):  # Using GISModelAdmin for geospatial fields
    list_display = ['address', 'bin_type', 'status', 'capacity', 'location']
    list_filter = ['bin_type', 'status']
    search_fields = ['address']
    ordering = ['address']

# WasteCollectionRequest Admin Setup
class WasteCollectionRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'collection_date', 'waste_type', 'status', 'priority', 'location']
    list_filter = ['status', 'priority']
    search_fields = ['user__username', 'address', 'waste_type']
    ordering = ['collection_date']

# WasteType Admin Setup
class WasteTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['name']

# CollectionPoint Admin Setup
class CollectionPointAdmin(GISModelAdmin):  # Using GISModelAdmin for geospatial fields
    list_display = ['name', 'address', 'status', 'capacity', 'location', 'collection_date']
    list_filter = ['status']
    search_fields = ['name', 'address']
    ordering = ['name']

# CollectionRequest Admin Setup
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'waste_type', 'collection_point', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['user__username', 'waste_type__name']
    ordering = ['created_at']

# Report Admin Setup
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'report_type', 'status', 'created_at', 'assigned_to']
    list_filter = ['status', 'report_type']
    search_fields = ['user__username', 'report_type']
    ordering = ['created_at']

# WasteAnalytics Admin Setup
class WasteAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['waste_type', 'total_collected', 'total_requests', 'average_collected_per_day', 'last_updated']
    list_filter = ['waste_type']
    search_fields = ['waste_type__name']
    ordering = ['waste_type__name']


# Register all models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(WasteBin, WasteBinAdmin)
admin.site.register(WasteCollectionRequest, WasteCollectionRequestAdmin)
admin.site.register(WasteType, WasteTypeAdmin)
admin.site.register(CollectionPoint, CollectionPointAdmin)
admin.site.register(CollectionRequest, CollectionRequestAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(WasteAnalytics, WasteAnalyticsAdmin)

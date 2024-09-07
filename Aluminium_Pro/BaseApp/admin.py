from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AluminumData, RealTimeMetric, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(AluminumData)  
class AluminumDataAdmin(admin.ModelAdmin):
    list_display = ('date', 'profile', 'wastage', 'loss', 'profit', 'recycled_weight', 'energy_consumption')
    search_fields = ('profile',)
    list_filter = ('date', 'profile')
    
@admin.register(RealTimeMetric)
class RealTimeMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_name', 'current_value', 'threshold_value', 'timestamp')
    search_fields = ('metric_name',)
    list_filter = ('timestamp',)
    

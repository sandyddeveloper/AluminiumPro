from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# CustomUser Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_admin(self):
        return self.role == 'admin'

    def is_user(self):
        return self.role == 'user'

# AluminumData Model
class AluminumData(models.Model):
    date = models.DateField(default=datetime.date.today)
    wastage = models.FloatField()
    loss = models.FloatField()
    profile = models.CharField(max_length=100)
    profit = models.FloatField()
    recycled_weight = models.FloatField()
    energy_consumption = models.FloatField()

    def __str__(self):
        return f"Data for {self.date} - {self.profile}"

# RealTimeMetric Model
class RealTimeMetric(models.Model):
    metric_name = models.CharField(max_length=100)
    current_value = models.FloatField()
    threshold_value = models.FloatField()
    alert_triggered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.metric_name} at {self.timestamp}"

# UserActivityLog Model

# Profile Model linked to CustomUser instead of User
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal to create or update Profile whenever CustomUser is saved
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    Profile.objects.get_or_create(user=instance)

class ProductionEfficiency(models.Model):
    date = models.DateField(default=datetime.date.today)
    temperature = models.FloatField()
    pressure = models.FloatField()
    production_output = models.FloatField()
    optimization_score = models.FloatField()
    
    def __str__(self):
        return f"Data for {self.date} - {self.optimization_score}"

class WastageAndLoss(models.Model):
    date = models.DateField(default=datetime.date.today)
    material_loss = models.FloatField()
    recyclability_score = models.FloatField()
    
    def __str__(self):
        return f"Data for {self.date} - {self.material_loss}"


    
class CostAndProfitability(models.Model):
    date = models.DateField(default=datetime.date.today)
    raw_material_cost = models.FloatField()
    energy_consumption = models.FloatField()
    labor_cost = models.FloatField()
    total_cost = models.FloatField(editable=False)  # Automatically calculated
    revenue = models.FloatField()  # Revenue needs to be provided
    profit_margin = models.FloatField(editable=False)  # Automatically calculated

    def __str__(self):
        return f"Data for {self.date} - {self.profit_margin}%"

    def save(self, *args, **kwargs):
        # Ensure revenue and total_cost are not None
        self.raw_material_cost = self.raw_material_cost or 0
        self.energy_consumption = self.energy_consumption or 0
        self.labor_cost = self.labor_cost or 0
        self.revenue = self.revenue or 0  # Default revenue to 0 if not provided
        
        # Calculate total cost
        self.total_cost = self.raw_material_cost + self.energy_consumption + self.labor_cost

        # Calculate profit margin, ensure no division by zero
        if self.revenue > 0:
            profit = self.revenue - self.total_cost
            self.profit_margin = (profit / self.revenue) * 100
        else:
            self.profit_margin = 0  # Set profit_margin to 0 if revenue is 0 or negative

        super().save(*args, **kwargs)




class EnvironmentalImpact(models.Model):
    date = models.DateField(default=datetime.date.today)
    carbon_footprint = models.FloatField()
    waste_management_efficiency = models.FloatField()
    
    def __str__(self):
        return f"Data for {self.date} - {self.waste_management_efficiency}"

class InventoryManagement(models.Model):
    date = models.DateField(default=datetime.date.today)
    raw_material_requirement = models.FloatField()
    current_inventory = models.FloatField()
    future_demand = models.FloatField(editable=False)  # Automatically calculated

    def save(self, *args, **kwargs):
        # Correct formula for future demand
        self.future_demand = round(self.raw_material_requirement - self.current_inventory, 2)
        super().save(*args, **kwargs)


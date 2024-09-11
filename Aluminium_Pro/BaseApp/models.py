from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class AluminumData(models.Model):
    date = models.DateField(default=datetime.date.today)
    wastage = models.FloatField()
    loss = models.FloatField()
    profile = models.CharField(max_length=100)
    profit = models.FloatField()
    recycled_weight = models.FloatField()
    energy_consumption = models.FloatField()

    def clean(self):
        if any(value < 0 for value in [self.wastage, self.loss, self.profit, self.recycled_weight, self.energy_consumption]):
            raise ValidationError("Values for wastage, loss, profit, recycled weight, and energy consumption must be non-negative.")

    def __str__(self):
        return f"Data for {self.date} - {self.profile}"


class RealTimeMetric(models.Model):
    metric_name = models.CharField(max_length=100, db_index=True)  # Indexed for performance
    current_value = models.FloatField()
    threshold_value = models.FloatField()
    alert_triggered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)  # Indexed for performance

    def clean(self):
        if self.current_value < 0 or self.threshold_value < 0:
            raise ValidationError("Current value and threshold value must be non-negative.")

    def __str__(self):
        return f"{self.metric_name} at {self.timestamp}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    job_position = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        instance.profile.save()


class ProductionEfficiency(models.Model):
    date = models.DateField(default=datetime.date.today)
    temperature = models.FloatField()
    pressure = models.FloatField()
    production_output = models.FloatField()
    optimization_score = models.FloatField()

    def clean(self):
        if not (0 <= self.optimization_score <= 100):
            raise ValidationError("Optimization score must be between 0 and 100.")

    def __str__(self):
        return f"Data for {self.date} - {self.optimization_score}"

# WastageAndLoss Model
class WastageAndLoss(models.Model):
    date = models.DateField(default=datetime.date.today)
    material_loss = models.FloatField()
    recyclability_score = models.FloatField()

    def clean(self):
        if self.material_loss < 0 or self.recyclability_score < 0:
            raise ValidationError("Material loss and recyclability score must be non-negative.")

    def __str__(self):
        return f"Data for {self.date} - {self.material_loss}"

class CostAndProfitability(models.Model):
    date = models.DateField(default=datetime.date.today)
    raw_material_cost = models.FloatField()
    energy_consumption = models.FloatField()  
    labor_cost = models.FloatField()
    total_cost = models.FloatField(editable=False)
    revenue = models.FloatField()
    profit_margin = models.FloatField(editable=False)

    def clean(self):
        if any(value < 0 for value in [self.raw_material_cost, self.energy_consumption, self.labor_cost, self.revenue]):
            raise ValidationError("Costs and revenue must be non-negative.")

    def save(self, *args, **kwargs):
        # Calculate total cost and round it to 2 decimal places
        self.total_cost = round(self.raw_material_cost + self.energy_consumption + self.labor_cost, 2)
        
        # Calculate and round the profit margin to 2 decimal places
        if self.revenue > 0:
            profit = self.revenue - self.total_cost
            self.profit_margin = round((profit / self.revenue) * 100, 2)
        else:
            self.profit_margin = 0
        
        # Round the energy consumption to 2 decimal places
        self.energy_consumption = round(self.energy_consumption, 2)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Data for {self.date} - {self.profit_margin}% profit"



class EnvironmentalImpact(models.Model):
    date = models.DateField(default=datetime.date.today)
    carbon_footprint = models.FloatField()
    waste_management_efficiency = models.FloatField()

    def clean(self):
        if self.carbon_footprint < 0 or self.waste_management_efficiency < 0:
            raise ValidationError("Carbon footprint and waste management efficiency must be non-negative.")

    def __str__(self):
        return f"Data for {self.date} - {self.waste_management_efficiency}"


class InventoryManagement(models.Model):
    date = models.DateField(default=datetime.date.today)
    raw_material_requirement = models.FloatField()
    current_inventory = models.FloatField()
    future_demand = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.future_demand = round(self.raw_material_requirement - self.current_inventory, 2)
        super().save(*args, **kwargs)

    def clean(self):
        if self.raw_material_requirement < 0 or self.current_inventory < 0:
            raise ValidationError("Raw material requirement and current inventory must be non-negative.")

    def __str__(self):
        return f"Data for {self.date} - {self.future_demand}"

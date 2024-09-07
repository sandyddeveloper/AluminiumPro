from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AluminumData, CustomUser, RealTimeMetric, Profile , ProductionEfficiency, WastageAndLoss, CostAndProfitability, EnvironmentalImpact, InventoryManagement
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', "password1", 'password2') 
        
        
class AluminumDataForm(forms.ModelForm):
    class Meta:
        model = AluminumData
        fields = ['date', 'wastage', 'loss', 'profile', 'profit', 'recycled_weight', 'energy_consumption']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'wastage': forms.NumberInput(attrs={'step': 0.01}),
            'loss': forms.NumberInput(attrs={'step': 0.01}),
            'profit': forms.NumberInput(attrs={'step': 0.01}),
            'recycled_weight': forms.NumberInput(attrs={'step': 0.01}),
            'energy_consumption': forms.NumberInput(attrs={'step': 0.01}),
        }


class RealTimeMetricForm(forms.ModelForm):
    class Meta:
        model = RealTimeMetric
        fields = ['metric_name', 'current_value', 'threshold_value']
        widgets = {
            'current_value': forms.NumberInput(attrs={'step': 0.01}),
            'threshold_value': forms.NumberInput(attrs={'step': 0.01}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        

class ProductionEfficiencyForm(forms.ModelForm):
    class Meta:
        model = ProductionEfficiency
        fields = ['date','temperature', 'pressure', 'production_output', 'optimization_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'temperature': forms.NumberInput(attrs={'step': 0.01}),
            'pressure': forms.NumberInput(attrs={'step': 0.01}),
            'production_output': forms.NumberInput(attrs={'step': 0.01}),
            'optimization_score': forms.NumberInput(attrs={'step': 0.01}),
            
        }
        
class WastageAndLossForm(forms.ModelForm):
    class Meta:
        model = WastageAndLoss
        fields = ['date', 'material_loss', 'recyclability_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'material_loss': forms.NumberInput(attrs={'step': 0.01}),
            'recyclability_score': forms.NumberInput(attrs={'step': 0.01}),
        }
        


class CostAndProfitabilityForm(forms.ModelForm):
    class Meta:
        model = CostAndProfitability
        fields = ['date', 'raw_material_cost', 'energy_consumption', 'labor_cost', 'revenue']  # Include 'revenue'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'raw_material_cost': forms.NumberInput(attrs={'step': 0.01}),
            'energy_consumption': forms.NumberInput(attrs={'step': 0.01}),
            'labor_cost': forms.NumberInput(attrs={'step': 0.01}),
            'revenue': forms.NumberInput(attrs={'step': 0.01}),  # Add 'revenue' input
        }


class EnvironmentalImpactForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalImpact
        fields = ['date', 'carbon_footprint','waste_management_efficiency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'carbon_footprint': forms.NumberInput(attrs={'step': 0.01}),
            'waste_management_efficiency': forms.NumberInput(attrs={'step': 0.01}),
        }
        


class InventoryManagementForm(forms.ModelForm):
    class Meta:
        model = InventoryManagement
        # Exclude 'future_demand' since it's automatically calculated
        fields = ['date', 'raw_material_requirement', 'current_inventory']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'raw_material_requirement': forms.NumberInput(attrs={'step': 0.01}),
            'current_inventory': forms.NumberInput(attrs={'step': 0.01}),
        }
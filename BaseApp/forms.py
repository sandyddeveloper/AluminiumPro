from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import (
    AluminumData, CustomUser, RealTimeMetric, Profile, ProductionEfficiency, 
    WastageAndLoss, CostAndProfitability, EnvironmentalImpact, InventoryManagement
)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class AluminumDataForm(forms.ModelForm):
    class Meta:
        model = AluminumData
        fields = ['date', 'wastage', 'loss', 'profile', 'profit', 'recycled_weight', 'energy_consumption']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'wastage': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'loss': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'profit': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'recycled_weight': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'energy_consumption': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }


class RealTimeMetricForm(forms.ModelForm):
    class Meta:
        model = RealTimeMetric
        fields = ['metric_name', 'current_value', 'threshold_value']
        widgets = {
            'current_value': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'threshold_value': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'avatar', 'phone_number', 'job_position', 'date_of_birth', 'gender', 'bio']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Number'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file'}),
            'job_position': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Bio', 'rows': 4}),
        }


class ProductionEfficiencyForm(forms.ModelForm):
    class Meta:
        model = ProductionEfficiency
        fields = ['date', 'temperature', 'pressure', 'production_output', 'optimization_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'temperature': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'pressure': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'production_output': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'optimization_score': forms.NumberInput(attrs={'step': 0.01, 'min': 0, 'max': 100}),
        }


class WastageAndLossForm(forms.ModelForm):
    class Meta:
        model = WastageAndLoss
        fields = ['date', 'material_loss', 'recyclability_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'material_loss': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'recyclability_score': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }


class CostAndProfitabilityForm(forms.ModelForm):
    class Meta:
        model = CostAndProfitability
        fields = ['date', 'raw_material_cost', 'energy_consumption', 'labor_cost', 'revenue']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'raw_material_cost': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'energy_consumption': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'labor_cost': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'revenue': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }


class EnvironmentalImpactForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalImpact
        fields = ['date', 'carbon_footprint', 'waste_management_efficiency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'carbon_footprint': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'waste_management_efficiency': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }

class InventoryManagementForm(forms.ModelForm):
    class Meta:
        model = InventoryManagement
        fields = ['date', 'raw_material_requirement', 'current_inventory']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'raw_material_requirement': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'current_inventory': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }

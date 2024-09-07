from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm , AluminumDataForm, RealTimeMetricForm ,ProfileForm, ProductionEfficiencyForm, WastageAndLossForm, EnvironmentalImpactForm, InventoryManagementForm, CostAndProfitabilityForm
from .models import ( RealTimeMetric,  AluminumData,  Profile, ProductionEfficiency, WastageAndLoss, CostAndProfitability, EnvironmentalImpact,InventoryManagement )
import json
import logging
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator


def homepage(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('custom_login')  # Redirect to login page or dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def admin_dashboard(request):
     
    if request.user.is_superuser:
        return render(request, 'admin/admin_dashboard.html')
    return redirect('user_dashboard')

@login_required
def user_dashboard(request):
    
    if request.user.is_user():
        return render(request, 'user/user_dashboard.html')
    return redirect('admin_dashboard')


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')  # Redirect superuser to admin dashboard
                else:
                    return redirect('user_dashboard')  # Redirect regular user to user dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('custom_login')

def admin_required(user):
    return user.is_authenticated and user.is_superuser

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import ProductionEfficiency, WastageAndLoss, CostAndProfitability, EnvironmentalImpact, InventoryManagement, AluminumData

@user_passes_test(admin_required)
@login_required
def admin_dashboard(request):
    # Fetch all records of models for placing the table in the admin dashboard
    production_table = ProductionEfficiency.objects.all()
    production_data = {
        "labels": [str(item.date) for item in production_table],
        "datasets": [
            {
                "label": "Temperature",
                "data": [item.temperature for item in production_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Pressure",
                "data": [item.pressure for item in production_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Production Output",
                "data": [item.production_output for item in production_table],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Optimization Score",
                "data": [item.optimization_score for item in production_table],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            }
        ]
    }
    
    #wastage table
    wastage_table = WastageAndLoss.objects.all()
    wastage_datas = {
        "labels": [str(item.date) for item in wastage_table],
        "datasets": [
            {
                "label": "Material Loss",
                "data": [item.material_loss for item in wastage_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Recyclability Score",
                "data": [item.recyclability_score for item in wastage_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
        ]
    }
    
    # Fetch all records from the CostAndProfitability model
    cop_table = CostAndProfitability.objects.all()

    # Prepare the data for the chart
    cop_datas = {
        "labels": [str(item.date) for item in cop_table],
        "datasets": [
            {
                "label": "Raw Material Cost",
                "data": [item.raw_material_cost for item in cop_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Energy Consumption",
                "data": [item.energy_consumption for item in cop_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Labor Cost",
                "data": [item.labor_cost for item in cop_table],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Total Cost",
                "data": [item.total_cost for item in cop_table],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            },
            {
                "label": "Profit Margin",
                "data": [item.profit_margin for item in cop_table],
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1
            }
        ]
    }
    
    # Fetch data from EnvironmentalImpact model
    envimpact_table = EnvironmentalImpact.objects.all()

    # Ensure there is data to pass
    if envimpact_table.exists():
        envimpact_datas = {
            "labels": [str(item.date) for item in envimpact_table],
            "datasets": [
                {
                    "label": "Carbon Footprint",
                    "data": [item.carbon_footprint for item in envimpact_table],
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Waste Management Efficiency",
                    "data": [item.waste_management_efficiency for item in envimpact_table],
                    "backgroundColor": "rgba(153, 102, 255, 0.2)",
                    "borderColor": "rgba(153, 102, 255, 1)",
                    "borderWidth": 1
                },
            ]
        }
    else:
        envimpact_datas = {"labels": [],"datasets": []}
        
    # Fetch data from the InventoryManagement model
    inventory_table = InventoryManagement.objects.all()

    # Ensure there is data to pass
    if inventory_table.exists():
        inventory_datas = {
            "labels": [str(item.date) for item in inventory_table],
            "datasets": [
                {
                    "label": "Raw Material Requirement",
                    "data": [item.raw_material_requirement for item in inventory_table],
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Current Inventory",
                    "data": [item.current_inventory for item in inventory_table],
                    "backgroundColor": "rgba(153, 102, 255, 0.2)",
                    "borderColor": "rgba(153, 102, 255, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Future Demand",
                    "data": [item.future_demand for item in inventory_table],
                    "backgroundColor": "rgba(255, 159, 64, 0.2)",
                    "borderColor": "rgba(255, 159, 64, 1)",
                    "borderWidth": 1
                }
            ]
        }
    else:
        # Default if no data available
        inventory_datas = {"labels": [], "datasets": []}

    # Fetch the latest records and reverse them before slicing
    aluminum_data = AluminumData.objects.order_by('-date')[:7][::-1]
    efficiency_data = ProductionEfficiency.objects.order_by('-date')[:7][::-1]
    wastage_data = WastageAndLoss.objects.order_by('-date')[:7][::-1]
    cost_profitability_data = CostAndProfitability.objects.order_by('-date')[:7][::-1]
    inventory_management_data = InventoryManagement.objects.order_by('-date')[:7][::-1]
    environmental_impact = EnvironmentalImpact.objects.all().order_by('-date')[:1][::-1]
    # Fetch latest data from each model for the radar chart with exception handling
    try:
        latest_efficiency = ProductionEfficiency.objects.latest('date')
    except ObjectDoesNotExist:
        latest_efficiency = None

    try:
        latest_wastage = WastageAndLoss.objects.latest('date')
    except ObjectDoesNotExist:
        latest_wastage = None

    try:
        latest_cost_profitability = CostAndProfitability.objects.latest('date')
    except ObjectDoesNotExist:
        latest_cost_profitability = None

    try:
        latest_environmental_impact = EnvironmentalImpact.objects.latest('date')
    except ObjectDoesNotExist:
        latest_environmental_impact = None

    try:
        latest_inventory = InventoryManagement.objects.latest('date')
    except ObjectDoesNotExist:
        latest_inventory = None

    # Prepare data for the radar chart
    radar_data = {
        "projected_efficiency": [90, 15, 85000, 80, 30000, 70],  # Replace with real projected data
        "actual_performance": [
            latest_efficiency.production_output if latest_efficiency else 0,
            latest_wastage.material_loss if latest_wastage else 0,
            latest_cost_profitability.profit_margin if latest_cost_profitability else 0,
            latest_efficiency.optimization_score if latest_efficiency else 0,
            latest_inventory.current_inventory if latest_inventory else 0,
            latest_environmental_impact.waste_management_efficiency if latest_environmental_impact else 0
        ]
    }

    # Prepare data for the line chart
    line_data = {
        "production_output": [data.production_output for data in efficiency_data],
        "recyclability": [data.recyclability_score for data in wastage_data],
        "material_loss": [data.material_loss for data in wastage_data],
        "dates": [data.date.strftime('%Y-%m-%dT%H:%M:%S.%fZ') for data in aluminum_data]
    }

    # Prepare data for the pie chart
    chart_data = [
        {"value": aluminum_data[-1].recycled_weight if aluminum_data else 0, "name": "Recycling"},
        {"value": wastage_data[-1].material_loss if wastage_data else 0, "name": "Wastage"},
        {"value": cost_profitability_data[-1].total_cost if cost_profitability_data else 0, "name": "Production Cost"},
        {"value": cost_profitability_data[-1].profit_margin if cost_profitability_data else 0, "name": "Profit"},
        {"value": inventory_management_data[-1].current_inventory if inventory_management_data else 0, "name": "Inventory"}
    ]

    context = {
        'aluminum_data': aluminum_data[0] if aluminum_data else None,
        'efficiency_data': efficiency_data[0] if efficiency_data else None,
        'wastage_data': wastage_data[0] if wastage_data else None,
        'cost_profit': cost_profitability_data [0] if cost_profitability_data  else None,
        'environmental_impact': environmental_impact[0] if environmental_impact else None,
        'inventory_management': inventory_management_data[0] if inventory_management_data else None,
        'line_data': line_data,
        'radar_data': radar_data,
        'chart_data': chart_data,
        "production_table": production_table,
        "production_data": json.dumps(production_data, cls=DjangoJSONEncoder),
        "wastage_table": wastage_table,
        "wastage_datas": json.dumps(wastage_datas, cls=DjangoJSONEncoder),
        'cop_table': cop_table,
        'cop_datas': json.dumps(cop_datas, cls=DjangoJSONEncoder),
        'envimpact_table': envimpact_table,
        'envimpact_datas': json.dumps(envimpact_datas, cls=DjangoJSONEncoder),
        'inventory_table': inventory_table,
        'inventory_datas': json.dumps(inventory_datas, cls=DjangoJSONEncoder),
    }

    return render(request, 'admin/admin_dashboard.html', context)




@login_required
def user_dashboard(request):
    # Fetch all records of models for placing the table in the admin dashboard
    production_table = ProductionEfficiency.objects.all()
    production_data = {
        "labels": [str(item.date) for item in production_table],
        "datasets": [
            {
                "label": "Temperature",
                "data": [item.temperature for item in production_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Pressure",
                "data": [item.pressure for item in production_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Production Output",
                "data": [item.production_output for item in production_table],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Optimization Score",
                "data": [item.optimization_score for item in production_table],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            }
        ]
    }
    
    #wastage table
    wastage_table = WastageAndLoss.objects.all()
    wastage_datas = {
        "labels": [str(item.date) for item in wastage_table],
        "datasets": [
            {
                "label": "Material Loss",
                "data": [item.material_loss for item in wastage_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Recyclability Score",
                "data": [item.recyclability_score for item in wastage_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
        ]
    }
    
    # Fetch all records from the CostAndProfitability model
    cop_table = CostAndProfitability.objects.all()

    # Prepare the data for the chart
    cop_datas = {
        "labels": [str(item.date) for item in cop_table],
        "datasets": [
            {
                "label": "Raw Material Cost",
                "data": [item.raw_material_cost for item in cop_table],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Energy Consumption",
                "data": [item.energy_consumption for item in cop_table],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Labor Cost",
                "data": [item.labor_cost for item in cop_table],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Total Cost",
                "data": [item.total_cost for item in cop_table],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            },
            {
                "label": "Profit Margin",
                "data": [item.profit_margin for item in cop_table],
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1
            }
        ]
    }
    
    # Fetch data from EnvironmentalImpact model
    envimpact_table = EnvironmentalImpact.objects.all()

    # Ensure there is data to pass
    if envimpact_table.exists():
        envimpact_datas = {
            "labels": [str(item.date) for item in envimpact_table],
            "datasets": [
                {
                    "label": "Carbon Footprint",
                    "data": [item.carbon_footprint for item in envimpact_table],
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Waste Management Efficiency",
                    "data": [item.waste_management_efficiency for item in envimpact_table],
                    "backgroundColor": "rgba(153, 102, 255, 0.2)",
                    "borderColor": "rgba(153, 102, 255, 1)",
                    "borderWidth": 1
                },
            ]
        }
    else:
        envimpact_datas = {"labels": [],"datasets": []}
        
    # Fetch data from the InventoryManagement model
    inventory_table = InventoryManagement.objects.all()

    # Ensure there is data to pass
    if inventory_table.exists():
        inventory_datas = {
            "labels": [str(item.date) for item in inventory_table],
            "datasets": [
                {
                    "label": "Raw Material Requirement",
                    "data": [item.raw_material_requirement for item in inventory_table],
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Current Inventory",
                    "data": [item.current_inventory for item in inventory_table],
                    "backgroundColor": "rgba(153, 102, 255, 0.2)",
                    "borderColor": "rgba(153, 102, 255, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Future Demand",
                    "data": [item.future_demand for item in inventory_table],
                    "backgroundColor": "rgba(255, 159, 64, 0.2)",
                    "borderColor": "rgba(255, 159, 64, 1)",
                    "borderWidth": 1
                }
            ]
        }
    else:
        # Default if no data available
        inventory_datas = {"labels": [], "datasets": []}

    # Fetch the latest records and reverse them before slicing
    aluminum_data = AluminumData.objects.order_by('-date')[:7][::-1]
    efficiency_data = ProductionEfficiency.objects.order_by('-date')[:7][::-1]
    wastage_data = WastageAndLoss.objects.order_by('-date')[:7][::-1]
    cost_profitability_data = CostAndProfitability.objects.order_by('-date')[:7][::-1]
    inventory_management_data = InventoryManagement.objects.order_by('-date')[:7][::-1]

    # Fetch latest data from each model for the radar chart with exception handling
    try:
        latest_efficiency = ProductionEfficiency.objects.latest('date')
    except ObjectDoesNotExist:
        latest_efficiency = None

    try:
        latest_wastage = WastageAndLoss.objects.latest('date')
    except ObjectDoesNotExist:
        latest_wastage = None

    try:
        latest_cost_profitability = CostAndProfitability.objects.latest('date')
    except ObjectDoesNotExist:
        latest_cost_profitability = None

    try:
        latest_environmental_impact = EnvironmentalImpact.objects.latest('date')
    except ObjectDoesNotExist:
        latest_environmental_impact = None

    try:
        latest_inventory = InventoryManagement.objects.latest('date')
    except ObjectDoesNotExist:
        latest_inventory = None

    # Prepare data for the radar chart
    radar_data = {
        "projected_efficiency": [90, 15, 85000, 80, 30000, 70],  # Replace with real projected data
        "actual_performance": [
            latest_efficiency.production_output if latest_efficiency else 0,
            latest_wastage.material_loss if latest_wastage else 0,
            latest_cost_profitability.profit_margin if latest_cost_profitability else 0,
            latest_efficiency.optimization_score if latest_efficiency else 0,
            latest_inventory.current_inventory if latest_inventory else 0,
            latest_environmental_impact.waste_management_efficiency if latest_environmental_impact else 0
        ]
    }

    # Prepare data for the line chart
    line_data = {
        "production_output": [data.production_output for data in efficiency_data],
        "recyclability": [data.recyclability_score for data in wastage_data],
        "material_loss": [data.material_loss for data in wastage_data],
        "dates": [data.date.strftime('%Y-%m-%dT%H:%M:%S.%fZ') for data in aluminum_data]
    }

    # Prepare data for the pie chart
    chart_data = [
        {"value": aluminum_data[-1].recycled_weight if aluminum_data else 0, "name": "Recycling"},
        {"value": wastage_data[-1].material_loss if wastage_data else 0, "name": "Wastage"},
        {"value": cost_profitability_data[-1].total_cost if cost_profitability_data else 0, "name": "Production Cost"},
        {"value": cost_profitability_data[-1].profit_margin if cost_profitability_data else 0, "name": "Profit"},
        {"value": inventory_management_data[-1].current_inventory if inventory_management_data else 0, "name": "Inventory"}
    ]

    usercontext = {
        'aluminum_data': aluminum_data[0] if aluminum_data else None,
        'efficiency_data': efficiency_data[0] if efficiency_data else None,
        'wastage_data': wastage_data[0] if wastage_data else None,
        'line_data': line_data,
        'radar_data': radar_data,
        'chart_data': chart_data,
        "production_table": production_table,
        "production_data": json.dumps(production_data, cls=DjangoJSONEncoder),
        "wastage_table": wastage_table,
        "wastage_datas": json.dumps(wastage_datas, cls=DjangoJSONEncoder),
        'cop_table': cop_table,
        'cop_datas': json.dumps(cop_datas, cls=DjangoJSONEncoder),
        'envimpact_table': envimpact_table,
        'envimpact_datas': json.dumps(envimpact_datas, cls=DjangoJSONEncoder),
        'inventory_table': inventory_table,
        'inventory_datas': json.dumps(inventory_datas, cls=DjangoJSONEncoder),
    }

    return render(request, 'user/user_dashboard.html', usercontext)


@login_required
def add_data(request):
    if request.method == 'POST':
        form = AluminumDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predict_aluminum')
    else:
        form = AluminumDataForm()
    return render(request, 'predictions/add_data.html', {'form': form})




@login_required
def monitor_metrics(request):
    metrics = RealTimeMetric.objects.all()

    # Check if any metric exceeds the threshold
    for metric in metrics:
        if metric.current_value > metric.threshold_value and not metric.alert_triggered:
            metric.alert_triggered = True
            metric.save()
            # Trigger an alert (e.g., send an email, or log it)
            print(f"Alert: {metric.metric_name} exceeded its threshold!")

    return render(request, 'predictions/monitor_metrics.html', {'metrics': metrics})

@login_required
def profile_view(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'predictions/profile.html', {'form': form})

@login_required
def add_aluminum_data(request):
    if request.method == 'POST':
        form = AluminumDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Ensure 'dashboard' is a valid URL name
    else:
        form = AluminumDataForm()
    return render(request, 'predictions/add_aluminum_data.html', {'form': form})




@login_required
def add_realtime_metric(request):
    if request.method == 'POST':
        form = RealTimeMetricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Ensure 'dashboard' is a valid URL name
    else:
        form = RealTimeMetricForm()
    return render(request, 'predictions/add_realtime_metric.html', {'form': form})






logger = logging.getLogger(__name__)

# Add Production Efficiency
def AddProductionEfficiencyViewSet(request):
    if request.method == 'POST':
        form = ProductionEfficiencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductionEfficiencyForm()
    return render(request, 'predictions/add_production_efficency.html', {'form': form})

# View Production Efficiency Data



@login_required
def ProductionEfficiencyViewSet(request):
    # Fetch all records of ProductionEfficiency and serialize them
    data = ProductionEfficiency.objects.all()  # Replace with your queryset
    chart_data = {
        "labels": [str(item.date) for item in data],
        "datasets": [
            {
                "label": "Temperature",
                "data": [item.temperature for item in data],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Pressure",
                "data": [item.pressure for item in data],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Production Output",
                "data": [item.production_output for item in data],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Optimization Score",
                "data": [item.optimization_score for item in data],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            }
        ]
    }
    context = {
        "data": data,
        "chart_data": json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'predictions/show_production_efficiency.html', context)



# Add Wastage and Loss
def AddWastageAndLossViewSet(request):
    if request.method == 'POST':
        form = WastageAndLossForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = WastageAndLossForm()
    return render(request, 'predictions/add_wastage_and_loss.html', {'form': form})

# View Wastage and Loss Data
@login_required
def WastageAndLossViewSet(request):
    data = WastageAndLoss.objects.all()
    chart_data = {
        "labels": [str(item.date) for item in data],
        "datasets": [
            {
                "label": "Material Loss",
                "data": [item.material_loss for item in data],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Recyclability Score",
                "data": [item.recyclability_score for item in data],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
        ]
    }
    context = {
        "data": data,
        "chart_data": json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'predictions/show_wastage_and_loss.html', context)


# Add Cost and Profitability
def AddCostAndProfitabilityViewSet(request):
    if request.method == 'POST':
        form = CostAndProfitabilityForm(request.POST)
        if form.is_valid():
            cost_data = form.save(commit=False)
            cost_data.save()
            return redirect('admin_dashboard')
    else:
        form = CostAndProfitabilityForm()
    return render(request, 'predictions/add_cost_and_profitability.html', {'form': form})

# View Cost and Profitability Data
@login_required
def CostAndProfitabilityViewSet(request):
    data = CostAndProfitability.objects.all()
    chart_data = {
        "labels": [str(item.date) for item in data],
        "datasets": [
            {
                "label": "Raw Material Cost", 
                "data": [item.raw_material_cost for item in data],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Energy Consumption", 
                "data": [item.energy_consumption for item in data],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Labor Cost",
                "data": [item.labor_cost for item in data],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            },
            {
                "label": "Total Cost",
                "data": [item. total_cost for item in data],
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            },
            {
                "label": "Profit Margin",
                "data": [item.profit_margin for item in data],
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1
            }
            
        ]
    }
    context = {
        "data": data,
        "chart_data": json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'predictions/show_cost_and_profitability.html', context)


# Add Environmental Impact
def AddEnvironmentalImpactViewSet(request):
    if request.method == 'POST':
        form = EnvironmentalImpactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EnvironmentalImpactForm()
    return render(request, 'predictions/add_environmental_impact.html', {'form': form})

# View Environmental Impact Data
@login_required
def EnvironmentalImpactViewSet(request):
    data = EnvironmentalImpact.objects.all()
    chart_data = {
        "labels": [str(item.date) for item in data],
        "datasets": [
            {
                "label": "Carbon Footprint",
                "data": [item.carbon_footprint for item in data],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Waste Management Efficiency",
                "data": [item.waste_management_efficiency for item in data],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
        ]
    }
    context = {
        "data": data,
        "chart_data": json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'predictions/show_environment_impact.html', context)


# Add Inventory Management
def AddInventoryManagementViewSet(request):
    if request.method == 'POST':
        form = InventoryManagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = InventoryManagementForm()
    return render(request, 'predictions/add_inventory_management.html', {'form': form})

# View Inventory Management Data
@login_required
def InventoryManagementViewSet(request):
    data = InventoryManagement.objects.all()
    chart_data = {
        "labels": [str(item.date) for item in data],
        "datasets": [
            {
                "label": "Raw Material Requirement",
                "data": [item. raw_material_requirement for item in data],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            },
            {
                "label": "Current Inventories",
                "data": [item.current_inventory for item in data],
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1
            },
            {
                "label": "Future Demand",
                "data": [item.future_demand for item in data],
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1
            }
        ]
    }
    context = {
        "data": data,
        "chart_data": json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'predictions/show_inventory_management.html', context)    



def search_results(request):
    # Get the query, model filter, and date range from the request
    query = request.GET.get('query', '')
    selected_model = request.GET.get('model', 'all')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    queries = query.split()  # Split the query into multiple keywords

    # Default: Fetch all data
    aluminum_data_results = AluminumData.objects.all()
    real_time_metric_results = RealTimeMetric.objects.all()
    production_efficiency_results = ProductionEfficiency.objects.all()
    cost_profitability_results = CostAndProfitability.objects.all()
    environmental_impact_results = EnvironmentalImpact.objects.all()
    inventory_management_results = InventoryManagement.objects.all()

    if query:
        # Apply filters for each keyword across all models or specific models
        for keyword in queries:
            if selected_model == 'AluminumData' or selected_model == 'all':
                aluminum_data_results = aluminum_data_results.filter(
                    Q(profile__icontains=keyword) | Q(date__icontains=keyword)
                )
            if selected_model == 'RealTimeMetric' or selected_model == 'all':
                real_time_metric_results = real_time_metric_results.filter(
                    Q(metric_name__icontains=keyword) | Q(timestamp__icontains=keyword)
                )
            if selected_model == 'ProductionEfficiency' or selected_model == 'all':
                production_efficiency_results = production_efficiency_results.filter(
                    Q(date__icontains=keyword) | Q(temperature__icontains=keyword) | Q(pressure__icontains=keyword)
                )
            if selected_model == 'CostProfitability' or selected_model == 'all':
                cost_profitability_results = cost_profitability_results.filter(
                    Q(date__icontains=keyword) | Q(revenue__icontains=keyword) | Q(profit_margin__icontains=keyword)
                )
            if selected_model == 'EnvironmentalImpact' or selected_model == 'all':
                environmental_impact_results = environmental_impact_results.filter(
                    Q(date__icontains=keyword) | Q(carbon_footprint__icontains=keyword)
                )
            if selected_model == 'InventoryManagement' or selected_model == 'all':
                inventory_management_results = inventory_management_results.filter(
                    Q(date__icontains=keyword) | Q(raw_material_requirement__icontains=keyword)
                )

    # Date range filter (if provided)
    if start_date and end_date:
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")

            if selected_model == 'AluminumData' or selected_model == 'all':
                aluminum_data_results = aluminum_data_results.filter(date__range=[start, end])
            if selected_model == 'RealTimeMetric' or selected_model == 'all':
                real_time_metric_results = real_time_metric_results.filter(timestamp__date__range=[start, end])
            if selected_model == 'ProductionEfficiency' or selected_model == 'all':
                production_efficiency_results = production_efficiency_results.filter(date__range=[start, end])
            if selected_model == 'CostProfitability' or selected_model == 'all':
                cost_profitability_results = cost_profitability_results.filter(date__range=[start, end])
            if selected_model == 'EnvironmentalImpact' or selected_model == 'all':
                environmental_impact_results = environmental_impact_results.filter(date__range=[start, end])
            if selected_model == 'InventoryManagement' or selected_model == 'all':
                inventory_management_results = inventory_management_results.filter(date__range=[start, end])
        except ValueError:
            pass  # Handle invalid date format gracefully

    # Pagination
    page_number = request.GET.get('page', 1)
    
    # Paginate each set of results independently
    aluminum_data_paginator = Paginator(aluminum_data_results, 10)
    real_time_metric_paginator = Paginator(real_time_metric_results, 10)
    production_efficiency_paginator = Paginator(production_efficiency_results, 10)
    cost_profitability_paginator = Paginator(cost_profitability_results, 10)
    environmental_impact_paginator = Paginator(environmental_impact_results, 10)
    inventory_management_paginator = Paginator(inventory_management_results, 10)

    # Get the paginated objects for the current page
    aluminum_data_page_obj = aluminum_data_paginator.get_page(page_number)
    real_time_metric_page_obj = real_time_metric_paginator.get_page(page_number)
    production_efficiency_page_obj = production_efficiency_paginator.get_page(page_number)
    cost_profitability_page_obj = cost_profitability_paginator.get_page(page_number)
    environmental_impact_page_obj = environmental_impact_paginator.get_page(page_number)
    inventory_management_page_obj = inventory_management_paginator.get_page(page_number)

    context = {
        'query': query,
        'selected_model': selected_model,
        'start_date': start_date,
        'end_date': end_date,
        'aluminum_data_page_obj': aluminum_data_page_obj,
        'real_time_metric_page_obj': real_time_metric_page_obj,
        'production_efficiency_page_obj': production_efficiency_page_obj,
        'cost_profitability_page_obj': cost_profitability_page_obj,
        'environmental_impact_page_obj': environmental_impact_page_obj,
        'inventory_management_page_obj': inventory_management_page_obj,
    }

    return render(request, 'search_results.html', context)
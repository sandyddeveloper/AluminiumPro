from django.urls import path
from . import views


urlpatterns = [
    
    #Home Page
    path('home/', views.homepage, name='homepage'),
    
    # Authentication
    path('', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),  
    path('logout/', views.logout_view, name='logout'),
    
    #Profile Section
    path('view_profile/', views.view_profile, name='view_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Data Entry by Admin
    path('add-aluminum-data/', views.add_aluminum_data, name='add_aluminum_data'),
    path('add-realtime-metric/', views.add_realtime_metric, name='add_realtime_metric'),
    path('add-production-efficiency/', views.AddProductionEfficiencyViewSet, name='add_production_efficiency'),
    path('add-wastage-and-loss/', views.AddWastageAndLossViewSet, name='add-wastage-and-loss'),
    path('add-cost-and-profitability/', views.AddCostAndProfitabilityViewSet, name='add-cost-and-profitability'),
    path('add-environmental-impact/', views.AddEnvironmentalImpactViewSet, name='add-environmental-impact'),
    path('add-inventory-management/', views.AddInventoryManagementViewSet, name='add-inventory-management'),
    
    #Serch enigine
    path('search/', views.search_results, name='search_results'),
    
    # Real-Time Monitoring and Alerts
    path('monitor-metrics/', views.monitor_metrics, name='monitor_metrics'),
    path('show-production-efficiency/', views.ProductionEfficiencyViewSet, name='show-production-efficiency'),
    path('show-wastage-and-loss/', views.WastageAndLossViewSet, name='show-wastage-and-loss'),
    path('show-inventory-management/', views.InventoryManagementViewSet, name='show-inventory-management'),
    path('show-cost-and-profitability/', views.CostAndProfitabilityViewSet, name='show-cost-and-profitability'),
    path('show-environmental-impact/', views.EnvironmentalImpactViewSet, name='show-environmental-impact'),

    # Password Reset (Django built-in views for password reset)
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>/', views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('success_page/', views.SuccessPage, name='success_page'),

   
]

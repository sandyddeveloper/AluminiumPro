from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    
    #Home Page
    path('home/', views.homepage, name='homepage'),
    
    # Authentication
    path('', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),  
    path('logout/', views.logout_view, name='logout'),
    
    path('profile/', views.profile_view, name='profile'),

    # Dashboard
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),

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
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

   
]

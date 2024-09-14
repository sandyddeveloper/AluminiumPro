from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from BaseApp.models import (AluminumData, RealTimeMetric, ProductionEfficiency, 
                          WastageAndLoss, CostAndProfitability, EnvironmentalImpact, InventoryManagement)

class Command(BaseCommand):
    help = 'Generate sample data for 2 days'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        for i in range(2):
            date = today - timedelta(days=i)

            # AluminumData
            AluminumData.objects.create(
                date=date,
                wastage=round(random.uniform(100, 200), 2),
                loss=round(random.uniform(50, 100), 2),
                profile=f"Profile_{i}",
                profit=round(random.uniform(1000, 5000), 2),
                recycled_weight=round(random.uniform(50, 100), 2),
                energy_consumption=round(random.uniform(500, 1000), 2)
            )

            # RealTimeMetric
            RealTimeMetric.objects.create(
                metric_name=f"Metric_{i}",
                current_value=round(random.uniform(50, 100), 2),
                threshold_value=round(random.uniform(60, 90), 2),
                alert_triggered=bool(random.getrandbits(1)),
                timestamp=timezone.now() - timedelta(days=i)
            )

            # ProductionEfficiency
            ProductionEfficiency.objects.create(
                date=date,
                temperature=round(random.uniform(300, 500), 2),
                pressure=round(random.uniform(1000, 1500), 2),
                production_output=round(random.uniform(200, 400), 2),
                optimization_score=round(random.uniform(50, 100), 2)
            )

            # WastageAndLoss
            WastageAndLoss.objects.create(
                date=date,
                material_loss=round(random.uniform(10, 50), 2),
                recyclability_score=round(random.uniform(0, 100), 2)
            )

            # CostAndProfitability
            raw_material_cost = round(random.uniform(1000, 2000), 2)
            energy_consumption = round(random.uniform(500, 1000), 2)
            labor_cost = round(random.uniform(300, 500), 2)
            revenue = round(random.uniform(3000, 6000), 2)

            cost_and_profit = CostAndProfitability.objects.create(
                date=date,
                raw_material_cost=raw_material_cost,
                energy_consumption=energy_consumption,
                labor_cost=labor_cost,
                revenue=revenue
            )
            cost_and_profit.save()  # Automatically calculates total_cost and profit_margin

            # EnvironmentalImpact
            EnvironmentalImpact.objects.create(
                date=date,
                carbon_footprint=round(random.uniform(100, 300), 2),
                waste_management_efficiency=round(random.uniform(50, 100), 2)
            )

            # InventoryManagement
            raw_material_requirement = round(random.uniform(1000, 2000), 2)
            current_inventory = round(random.uniform(500, 1500), 2)
            InventoryManagement.objects.create(
                date=date,
                raw_material_requirement=raw_material_requirement,
                current_inventory=current_inventory
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 2 days of sample data.'))

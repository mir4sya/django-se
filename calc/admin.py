from django.contrib import admin
from .models import  OrderData, SalesReport, Food, Tsales, DailySales, WeeklySales, MonthlySales, FoodData

# Register your models here.

admin.site.register(OrderData)
admin.site.register(SalesReport)
admin.site.register(Food)
admin.site.register(Tsales)
admin.site.register(DailySales)
admin.site.register(MonthlySales)
admin.site.register(WeeklySales)
admin.site.register(FoodData)

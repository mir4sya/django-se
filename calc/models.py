from django.db import models

# Create your models here.
    
class FoodData(models.Model):
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField()
    price = models.FloatField()

class OrderData(models.Model):
    foodName = models.CharField(max_length = 100)
    foodPrice = models.FloatField()
    quantity =  models.FloatField()
    
class SalesReport(models.Model):
    sales = models.CharField(max_length = 100)
    totalSales = models.FloatField()

class Food(models.Model):
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField()
   

class Tsales(models.Model):
    noId = models.PositiveIntegerField()
    day = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    
class DailySales(models.Model):
    noId = models.PositiveIntegerField()
    dayly = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    
class WeeklySales(models.Model):
    noId = models.PositiveIntegerField()
    weekly = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    
class MonthlySales(models.Model):
    noId = models.PositiveIntegerField()
    monthly = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    

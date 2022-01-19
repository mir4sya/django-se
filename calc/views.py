from django.shortcuts import render
from django.http import HttpResponse
from .models import  Food, Tsales,  DailySales, MonthlySales, WeeklySales, FoodData
# Create your views here.

def home(request):
    
    labels =[]
    data = []
    pri = []
    
    queryset = FoodData.objects.order_by('-qty')[:5]
    for food in queryset:
        labels.append(food.name)
        data.append(food.qty)
        pri.append(food.price)

    return render(request,'home.html', {
        'labels': labels,
        'data':data,
        'pri':pri,
    })
def highest(request):
    labels =[]
    data = []
    
    queryset = Food.objects.order_by('-qty')[:5]
    for food in queryset:
        labels.append(food.name)
        data.append(food.qty)

    return render(request,'highest.html', {
        'labels': labels,
        'data':data
    })
    
        

def lowest(request):
    
    labels =[]
    data = []
    
    queryset = Food.objects.order_by('qty')[:5]
    for food in queryset:
        labels.append(food.name)
        data.append(food.qty)
    
    
    return render(request,'lowest.html', {
        'labels': labels,
        'data':data
    })

def daily(request):
    
    labels =[]
    data = []
    
    queryset = DailySales.objects.order_by('noId')[:5]
    for sal in queryset:
        labels.append(sal.dayly)
        data.append(sal.sales)
    
    
    return render(request,'daily.html', {
        'labels': labels,
        'data':data
    })

def weekly(request):
    
    labels =[]
    data = []
    
    queryset = WeeklySales.objects.order_by('noId')[:5]
    for sal in queryset:
        labels.append(sal.weekly)
        data.append(sal.sales)
    
    
    return render(request,'weekly.html', {
        'labels': labels,
        'data':data
    })


def monthly(request):
    
    labels =[]
    data = []
    
    queryset = MonthlySales.objects.order_by('noId')[:12]
    for sal in queryset:
        labels.append(sal.monthly)
        data.append(sal.sales)
    
    
    return render(request,'monthly.html', {
        'labels': labels,
        'data':data
    })


def total(request):
    
    labels =[]
    data = []
    
    queryset = Tsales.objects.order_by('noId')[:5]
    for sal in queryset:
        labels.append(sal.day)
        data.append(sal.sales)
    
    
    return render(request,'totalsales.html', {
        'labels': labels,
        'data':data
    })

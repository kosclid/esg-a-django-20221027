from django.shortcuts import render
from diary.models import Memory

def index(request):
    dia_qs = Memory.objects.all().order_by('-pk')
    return render(
        request, 
        "diary/memory_list.html",
        {'dia_list' : dia_qs,
        })

def dia_detail(request, pk):
    dtail = Memory.objects.get(pk = pk)
    return render(
        request, 
        "diary/memory_detail.html",
        {'dtl' : dtail,
        })
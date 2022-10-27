from django.shortcuts import render
from diary.models import Memory

def index(request):
    # 전체 포스팅을 가져올 준비(가져오기 이전임)
    dia_qs = Memory.objects.all().order_by('-pk')
    return render(
        request, 
        "diary/memory_list.html",
        {'dia_list' : dia_qs,
        }
        )
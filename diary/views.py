from django.shortcuts import render, redirect
from diary import forms
from diary.models import Memory
from diary.forms import DiaForm
from django.views.generic import CreateView


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

def dia_new(request):
    if request.method =="GET":
        form = DiaForm()  # 인자 없이 주면 빈 폼이다.
    else:
        form = DiaForm(request.POST)  # 입력된 값은 request.POST에 저장 되어있다.
        if form.is_valid():  # 유효성 검사 함수 단하나라도 통과 못하면 거짓을 반환
            memory = form.save()  # ModelForm에서 지원
            # return redirect(f'/diary/{memory.pk}/')

            # return redirect(memory.get_absolute_url())
            return redirect(memory)

    return render(request, 'diary/memory_new.html', {
        'form' : form,
    })
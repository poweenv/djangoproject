from django.shortcuts import render,redirect
from ..models import readingList
from ..forms import ReadingForm

from django.utils import timezone
from django.contrib.auth.decorators import login_required

def report_create(request):
    """
    독서 후기 등록
    """
    if request.method =="POST":
        form = ReadingForm(request.POST,request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.author= request.user
            report.save()
            return redirect("book:index")
    else:
        form = ReadingForm()
    return render(request,"book/report_create.html",{"form":form})
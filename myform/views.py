from urllib.request import Request
from django.shortcuts import render
from django.template import RequestContext
from.import forms
# Create your views here.
def student_view(request):
    form=forms.studentform()
    if request.method=='POST':
        form=forms.studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'myform/home.html',{'form':form})
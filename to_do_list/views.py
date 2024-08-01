from django.shortcuts import render,redirect
from .models import *
# from django.http import HttpResponse
# Create your views here.
def todo(request):
    if request.method=="POST":
        data=request.POST
        todo_heading=data.get('todo_heading')
        todo_description=data.get('todo_description')
        to_do.objects.create(
            todo_heading=todo_heading,
            todo_description=todo_description,
        )
        return redirect('/todo')
    
    queryset=to_do.objects.all()
    context={"todo":queryset}

    return render(request,'index.html',context)


def delete_todo(request,id):
    print(id)
    queryset =to_do.objects.get(id=id)
    queryset.delete()
    return redirect('/todo/')

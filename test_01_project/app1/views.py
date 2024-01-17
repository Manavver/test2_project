from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Actor
# Create your views here.


def actor_list(request):
    a=Actor.objects.all()
    return render(request,'app1/actor_list1.html',{'a':a})

def testing(request):
    a = Actor.objects.all()
    return render(request,'app1/testing.html',{'a':a})
def testing2(request):
    a = Actor.objects.all()
    return render(request,'app1/testing2.html',{'a':a})


def data_post(request):
    if request.method=="POST":
        A=Actor()
        A.Name=request.POST['name']
        A.details=request.POST['details']

        A.save()
        #return render(request, 'post.html')
        return redirect('/app1/actor_list/')
    else:
        return render(request, 'post.html')
"""
def edit(request, id):
    a = Actor.objects.get(id=id)
    return render(request, 'edit.html', {'a': a})





def RecordEdited(request ,id):
    #A = get_object_or_404(Actor, id=id)
    #if request.method=='POST':
        #A= get_object_or_404(Actor,id=id)
        Name = request.POST.get['name']
        details = request.POST.get['details']
        actor=Actor(Name=Name,details=details)
        actor.save()
        return redirect('/app1/actor_list/')
    #return render(request,'edit.html')

    #else:
        #return HttpResponse("page not found")"""


def delete(request, id):
    A = Actor.objects.get(id=id)
    print(A)
    b=A.delete()
    print(b)
    return redirect("/app1/actor_list/")

def update_std(request,id):
    std=Actor.objects.get(id=id)
    print(std)
    return render(request,'update_std.html',{'std':std})

def do_update_std(request ,id):
    Name = request.POST.get('name')
    details = request.POST.get('details')
    std=Actor.objects.get(pk=id)
    print(std)
    std.Name=Name
    std.details=details

    std.save()
    print(std.Name)
    print(std.details)

    return redirect('/app1/actor_list/')

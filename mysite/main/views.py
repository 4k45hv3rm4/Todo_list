from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import  Item
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

@login_required(login_url="/login/")
def create(request):
    print(request.POST)
    if request.method=="POST":

        form = TaskForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['task']
            c = form.cleaned_data['complete']
            x = Item(user=request.user, task=t, complete=c)
            x.save()
            return redirect("/home/")
    else:
            form = TaskForm()

    return render(request, "create.html",{'form':form} )


@login_required(login_url="/login/")
def home(request):

    todolist = Item.objects.filter(user=request.user).filter(complete=False)
    length = len(todolist)
    if request.method=="POST":
        if request.POST.get('save'):

            for i in todolist:
                if request.POST.get("c"+str(i.id))=="clicked":
                    i.complete=True
                    i.save()
                    return redirect("/home/")
                else:
                    i.complete=False

        elif request.POST.get('newTask'):
            txt = request.POST.get("new")
            if len(txt)>2:
                todolist.create(task=txt, complete
                =False)
            else:
                print("Invalid")

    return render(request, "base.html", {"todolist":todolist, 'length':length})

@login_required(login_url="/login/")
def completed_task(request):
    todolist = Item.objects.filter(user=request.user).filter(complete=True)
    length = len(todolist)
    if request.method=="POST":
        if request.POST.get('save'):

            for i in todolist:
                if request.POST.get("c"+str(i.id))=="clicked":
                    i.complete=False
                    i.save()
                    return redirect("/completed_task/")
                else:

                    i.complete=True

        elif request.POST.get('newTask'):
            txt = request.POST.get("new")
            if len(txt)>2:
                todolist.create(task=txt, complete
                =False)
            else:
                print("Invalid")

    return render(request, "base.html", {'todolist':todolist, 'length':length})


class  task_delete(DeleteView):
    model = Item
    template_name="confirm_delete.html"
    success_url = reverse_lazy("home")



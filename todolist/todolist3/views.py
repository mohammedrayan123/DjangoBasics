from django.shortcuts import render,redirect
from .models import TodoList
# todolist=[]
def index(request):

    # if request.POST:
    #     new_task = request.POST['task']
    #     todolist.append(new_task.strip())
    #     return redirect('index')
    # return render(request,'todolist2/index.html',context={'task':todolist})
    if request.POST:
        new_task = request.POST['task'].strip()
        description = request.POST['desc'].strip()
        todolist=TodoList(taskTitle=new_task, taskDesc=description)
        todolist.save()
        return redirect('index')
    
    todolist=TodoList.objects.all()
    return render(request,'todolist2/index.html',context={'task':todolist})

def deleteTask(request,id):
    task=TodoList.objects.get(taskid=id)
    task.delete()
    return redirect('index')

def editTask(request,id):
    task=TodoList.objects.get(taskid=id)
    if request.POST:
        new_task = request.POST['task'].strip()
        description = request.POST['desc']
        task.taskTitle=new_task
        task.taskDesc=description
        task.save()
        return redirect('index')
    return render(request,'todolist2/edit.html',context={'task':task})

# Create your views here.

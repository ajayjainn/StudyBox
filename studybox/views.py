from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    users = []
    respTaskComp= []

    for user in User.objects.all():
        users.append(user.username)
        respTaskComp.append(len(user.task_set.all()))
    
    context = {'allUsernames':users, 'tasksCompleted':respTaskComp}
    return render(request, 'studybox/index.html', context)

def signin(request):
    if request.method=='GET':
        return render(request, 'studybox/signin.html')
    
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request,'Invalid username or password.')
            return redirect('signin')

def logout_(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect('home')

def tasks(request):
    if request.method=='GET':

        #If user wants to access data of particular username
        username = request.GET.get('name',None)
        if username:
            user = User.objects.get(username=username)

        #User simply wants to access information
        else:
            if request.user.is_authenticated: #His own information
                user = request.user
            else:   #Wants to access anonymously
                user = User.objects.all()[1]

        completed_tasks = [task for task in Task.objects.filter(completed_by=user)]
        incomplete_tasks = [task for task in Task.objects.all() if task not in completed_tasks]
        totalTasks = len(completed_tasks + incomplete_tasks)
        allUsernames = [user.username for user in User.objects.all()]
        if not totalTasks==0:
            context =  {
                'name':user.username,
                'completed':completed_tasks,
                'incomplete':incomplete_tasks,
                'totalTasks':len(completed_tasks) + len(incomplete_tasks),
                'completedTasks':len(completed_tasks),
                'incompleteTasks':len(incomplete_tasks),
                'percentage':int(len(completed_tasks)/totalTasks*100),
                'allUsernames': allUsernames
                }
        else: # If there are 0 tasks available
            context = {}
        return render(request, 'studybox/tasks.html', context=context)

    else: # Wants to update information # Post request

        if not request.user.is_authenticated:
            messages.error(request,'Please login first')
            return redirect('signin')
    
        task_id = request.POST.get('id',None)
        if task_id: # User has completed a Task
            task = Task.objects.get(pk=task_id)
            task.completed_by.add(request.user)
            messages.success(request,'Congratulations for completing the task.')  

        taskTitle = request.POST.get('tasktitle',None)
        if taskTitle: #User wants to add a new task
            task = Task(title=taskTitle)
            task.save()
            messages.success(request,'Task Created Successfully.')

        return redirect('/tasks')

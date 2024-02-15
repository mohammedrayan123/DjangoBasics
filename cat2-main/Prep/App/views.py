from django.shortcuts import render, redirect
from .models import New_User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        pass1 = request.POST.get('password')

        user = authenticate(request,username=username,password=pass1)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request, 'main/index.html', {'error_message': 'Invalid credentials'})
            print(error_message)

    return render(request,'main/index.html')

def register(request):
    if request.method == 'POST':
        Reg = request.POST.get('reg')
        Name = request.POST.get('full_name')
        Email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        Age = request.POST.get('age')
        pass1 = request.POST.get('pass')
        
        my_user = User.objects.create_user(username=Email,email=Email, password=pass1)
        my_user.save()

        Regs = New_User(
            user=my_user,
            reg_no=Reg,
            name=Name,
            email=Email, 
            phone=Phone,
            age=Age)
        Regs.save() 

        return redirect('index')
    return render(request,'main/reg.html')

# def profile(request):
#     user_id = request.user.id
#     try:
#         data = New_User.objects.get(id=user_id)
#     except New_User.DoesNotExist:
#         # Handle the case where the user doesn't exist
#         return redirect('index')  # Redirect to homepage or handle appropriately
#     except:
#         data = None  # Assign None if an unexpected error occurs
#     return render(request, 'main/profile.html', {'data': data})




@login_required
def profile(request):
        user_id = request.user # Assuming user_id is the primary key
        data = New_User.objects.get(user=user_id)
        return render(request, 'main/profile.html', {'data': data})

def editprofile(request,id):
    user_id = request.user
    data = New_User.objects.get(user=user_id)
    if request.POST:
        editReg = request.POST.get('reg')
        editName = request.POST.get('full_name')
        editEmail = request.POST.get('email')
        editPhone = request.POST.get('Phone')
        editAge = request.POST.get('age')
        print(editAge)
        data.reg_no=editReg
        data.name=editName
        data.email=editEmail
        data.phone=editPhone
        data.age=editAge
        data.save()
        return redirect('profile')
    return render(request,'main/editprofile.html',context={'data':data})

def deleteuser(request,id):
    deldata=New_User.objects.get(user=id)
    deldata.delete()
    return redirect('index')
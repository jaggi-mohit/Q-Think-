from userdata.models import Userdata
from showdata.models import showdata,ans
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Userdetail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime




def signup(request):
    if request.method=="POST":
        name=request.POST['Fname']
        email=request.POST['email']
        password1=request.POST['passw']
        age1=request.POST['age']
        gender=request.POST.get('gridRadios')
        if User.objects.filter(username=email):
            messages.error(request,f'Email Already Exists!Try Another or Login!')
            return redirect('signup')
        else:    
            x = User.objects.create_user(username=email,password=password1,first_name=name)
            auth.login(request,x)
            z=request.user
            userdata=Userdetail(age=age1,gender=gender,user_id=z.id)
            userdata.save()
            x.save()
            points = Userdetail.objects.get(user_id=z.id)
            
            messages.success(request,f'Welcome {x}! Account Created Kindly Login!{points.userpoints}')
            return redirect('login')
        
    
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        mail = request.POST['email1']
        password = request.POST['passw']
        user=auth.authenticate(username=mail,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,f'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')


def home(request):
    user1=request.user
    if request.user.is_anonymous:
        messages.info(request,f'Kindly Login!')
        return redirect('login')
    if user1 is not None:
        print(user1)
        datas=showdata.objects.all()
        ans1= ans.objects.all()
        time = datetime.now()
        current_time = time.strftime("%H:%M")
        timehour =int(time.strftime("%H"))
        print(timehour)
        if timehour >= 13:
            hour = "pm";
        if timehour < 13:
            hour = "am"
           
        
        
      

        
        return render(request,'home.html',{'ans': datas,'ans1':ans1,'user':user1,'time':current_time,'hour':hour,'request':request})

@login_required(login_url='login/')
def profile(request):
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = Userdetail.objects.get(user_id=uid.id)
        t.profile_img=url
        t.save()

        
    datas=Userdetail.objects.filter(user=request.user)
    return render(request,'profile.html',{'data':datas})

def logout(request):
    auth.logout(request)
    messages.info(request,f'Logged Out Successfully!')
    return redirect('login')
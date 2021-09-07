from login.models import Userdetail
from django.contrib import messages
from showdata.models import ans
from showdata.models import showdata
from django.shortcuts import render,redirect
from .models import Userdata
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
'''
def addqtn(request):
    if request.method == "POST":
        ans = request.POST['txtarea']
        y= request.user
        x = Userdata(ans=ans,user_id=y.id)
        x.save()
        z = showdata(answers=ans,username=y)
        z.save()
        datas=showdata.objects.all()
        return render(request,'home.html',{'ans': datas})
'''
def add(request, pk):
    if request.method =="POST":
        answ = request.POST['txtarea']
        z=request.user
        x = ans(answers=answ,username=z,qtn_id=pk)
        y = Userdata(ans=ans,user_id=z.id)
        #k= showdata(username=z)
        #k.save()
        y.save()
        addpoints= Userdetail.objects.get(user_id=z.id)
        addpoints.userpoints += 1
        addpoints.save()
        x.save()
        messages.info(request,f'Answer is added successfully! Your Points are{addpoints.userpoints}')
        return redirect('home')
    else:
        return render(request,'edit.html',{'add':pk})


def delete(request,pk):
    item = ans.objects.get(id=pk)
    item.delete()
    messages.info(request,f"Answer Deleted Successfully!")
    return redirect('home')
    
@login_required(login_url='login/')
def edit(request,pk):
    if request.method == "POST":
        z = request.user
        x = request.POST['txtarea']
        item = ans.objects.get(id=pk)
        y = Userdata(ans=x,user_id=z.id)
        y.save()
        item.answers = x
        item.save()
        messages.info(request,f"Answer Edited Successfully!")
        return redirect('home')
    return render(request,'edit.html',{'data':pk})

@login_required(login_url='login/')
def delqtn(request,pk):
    item = showdata.objects.get(id=pk)
    item.delete()
    messages.info(request,f"Question is been Deleted Successfully!")
    return redirect('home')

@login_required(login_url='login/')
def addquestion(request):
    z = request.user
    if request.method == "POST":
        userpoints = Userdetail.objects.get(user_id=z.id)
        
        if userpoints.userpoints <= 0:
            messages.info(request,f"Sorry U can't add question your points are 0")
            return redirect('home')
        
        x = request.POST['txtarea']
        item = showdata(username=z.username)
        y = Userdata(question=x,user_id=z.id)
        y.save()
        item.question = x
        item.save()
        userpoints.userpoints -=1
        userpoints.save()
        messages.info(request,f"Question Added Successfully!{userpoints.userpoints}")
        return redirect('home')
    return render(request,'edit.html',{'question':z})

'''
def addans(request):
    z = request.user
    if request.method == "POST":
        userpoints = Userdetail.objects.get(user_id=z.id)
        
        if userpoints.userpoints <= 0:
            messages.info(request,f"Sorry U can't add question your points are 0")
            return redirect('home')
        
        x = request.POST['txtarea']
        item = showdata(username=z.username)
        y = Userdata(question=x,user_id=z.id)
        y.save()
        item.question = x
        item.save()
        userpoints.userpoints -=1
        userpoints.save()
        messages.info(request,f"Question Added Successfully!{userpoints.userpoints}")
        return redirect('home')
    return render(request,'edit.html',{'question':z})

'''

def likes(request,pk):
    z = request.user
    like =  ans.objects.get(id=pk)
    if like.likebyuserby != z.username:
        like.likebyuserby=z.username
        like.likes += 1
        like.save()
        messages.info(request,f'Liked Added By {z}')
        return redirect("home")

    if like.likebyuserby == z.username:
        messages.info(request,f'Unliked!')
        like.likes -= 1 
        like.likebyuserby= None
        like.save()
        return redirect("home")
    
    
def dislikes(request,pk):
    z = request.user
    dis =  ans.objects.get(id=pk)
    if dis.disbyuser != z.username:
        dis.disbyuser=z.username
        dis.dislikes += 1
        dis.save()
        messages.info(request,f'DisLiked Added By {z}')
        return redirect("home")

    if dis.disbyuser == z.username:
        messages.info(request,f'Disliked Removed!')
        dis.dislikes -= 1 
        dis.disbyuser= None
        dis.save()
        return redirect("home")

        
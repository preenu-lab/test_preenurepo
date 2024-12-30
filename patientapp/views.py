from django.shortcuts import render,redirect

from django.http import request,HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout


def index(request):
    if (request.method == 'POST'):
        e = request.POST.get('tbEmail')
        p = request.POST.get('tbPassword')
        user = authenticate(request, username=e, password=p)
        if user:
            login(request, user)
            return HttpResponseRedirect('patienthome')
        else:
            return render(request, 'patient/login.html', {'result': "Invalid id and password"})
    return render(request, 'patient/login.html')




def signupview(request):
    if(request.method=='POST'):
        n=request.POST.get('tbName')
        e = request.POST.get('tbEmail')
        p = request.POST.get('tbPassword')
        p=make_password(p)
        try:
         rec=User.objects.create(first_name=n,email=e,password=p,username=e)
         rec.save()
         return render(request,'patient/signup.html',{'msg':'Thanks for register with us now you can login'})
        except:
           return render(request, 'patient/signup.html', {'msg': 'failed to insert record try again'})

    else:

       return  render(request,'patient/signup.html')

@login_required
def patient_home(request):
    patientemail=request.user
    records=DietDetails.objects.filter(user=patientemail)
    context={'data':records}
    return render(request,'patient/patient_home.html',context)


def logoutview(request):
        logout(request)
        return redirect('/')

@login_required
def add_diet(request):
    if (request.method == 'POST'):
        foodname = request.POST.get('tbFoodName')
        foodtimings = request.POST.get('tbHiddenTime')
        fooddays = request.POST.get('tbHiddenDays')
        foodduration = request.POST.get('tbDuration')
        print("ffffffffffffffffffffff---",fooddays)
        try:
            rec = DietDetails.objects.create(fooditem=foodname, user=request.user, foodtimes=foodtimings, foodtakenday=fooddays,takenduration=foodduration)
            rec.save()
            return render(request, 'patient/add_diet.html', {'msg': 'Your  record have been saved'})
        except Exception as ex:
            print("errrrrrrrrrrrrr--",ex)
            return render(request, 'patient/add_diet.html', {'msg': 'failed to insert record try again'})

    else:
       return render(request, 'patient/add_diet.html')



def delete_diet_view(request):
    sid=request.GET.get('id')

    DietDetails.objects.filter(id=sid).delete()

    return redirect('/patienthome')

def edit_diet_view(request):
    if(request.method=='POST'):
        sid=request.POST.get('tbId')
        foodname = request.POST.get('tbFoodName')

        foodtimings = request.POST.get('tbHiddenTime')

        fooddays = request.POST.get('tbHiddenDays')
        foodduration = request.POST.get('tbDuration')
        print("ffffffffffffffffffffff---", fooddays)
        try:
            rec = DietDetails.objects.get(id=sid)
            rec.fooditem=foodname
            rec.foodtimes=foodtimings
            rec.foodtakenday=fooddays
            rec.takenduration=foodduration
            rec.save()
            return redirect('/patienthome')
        except Exception as ex:
            print(ex)
    else:

     sid=request.GET.get('id')
     records=DietDetails.objects.get(id=sid)
     context={'data':records}
     return render(request,'patient/editdiet.html',context)
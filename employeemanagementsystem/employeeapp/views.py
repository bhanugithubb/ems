from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,reverse,get_object_or_404
from employeeapp.forms import UserForm
from django.contrib.auth.models import User
# Create your views here.

def employee_list(request):
    user=User.objects.all()
    return render(request,'employeeapp/index.html',{'user':user})

def employee_details(request,id=None):
    user_single=User.objects.get_object_or_404(id=id)
    return render(request,'employeeapp/employee_details.html',{'user_single':user_single})

def employee_add(request):
        if request.method=="POST":
            user_form=UserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return HttpResponseRedirect(reverse('employee_list'))
            else:
                return render(request,'employeeapp/employee_add.html',{'user_form':user_form})
        else:
            user_form=UserForm()
            return render(request,'employeeapp/employee_add.html',{'user_form':user_form})

def employee_edit(request,id=None):
    user= get_object_or_404(User,id=id)
    if request.method=="POST":
        user_form=UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employeeapp/edit.html',{'user_form':user_form})
    else:
        user_form=UserForm(instance=user)
        return render(request,'employeeapp/edit.html',{'user_form':user_form})

def employee_delete(request,id=None):
    user= get_object_or_404(User,id=id)
    if request.method=="POST":
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        return render(request,'employeeapp/delete.html',{'user':user})
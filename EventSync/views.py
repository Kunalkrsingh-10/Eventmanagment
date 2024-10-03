from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employees_info


def create(request):
    if request.method == 'POST':
        name = request.POST.get('emp_name')
        email = request.POST.get('emp_email')
        mob_no = request.POST.get('mob_no')
        new_employee = employees_info(name=name, email=email, Mob_no=mob_no)
        new_employee.save()
        return redirect('retrieve_emp')  
    else:
        return render(request, 'create_emp.html') 
def retrieve_emp(request):
    employess_data=employees_info.objects.all()
    context={'emp_all_data': employess_data}
    return render(request, 'retrieve_data.html', context)

def delete_emp(request,emp_id):
    new_emp=employees_info.objects.filter(id=emp_id).delete()
    if new_emp:
        return redirect('retrieve_emp')

def update_emp(request,emp_id):
    if request.method=='POST':
        name = request.POST.get('emp_name')
        email = request.POST.get('emp_email')
        mob_no = request.POST.get('mob_no')
        update=employees_info.objects.filter(id=emp_id).update(name=name, email=email, Mob_no=mob_no)
        if update: 
            return redirect('retrieve_emp')
    else:
       employee=employees_info.objects.get(id=emp_id)
       context = {"update_emp_data": employee}
       return render(request ,'update.html', context)

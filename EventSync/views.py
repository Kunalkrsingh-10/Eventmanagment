from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employees_info
from django.db import transaction
import threading

def create(request):
    if request.method == 'POST':
        name = request.POST.get('emp_name')
        email = request.POST.get('emp_email')
        mob_no = request.POST.get('mob_no')

        current_thread = threading.current_thread().name
        print(f"View of current thread : {current_thread}")

        try:
            with transaction.atomic():
                new_employee = employees_info(name=name, email=email, Mob_no=mob_no)
                new_employee.save()  
        except Exception as e:
            print(f"Transaction failed: {e}")
            return HttpResponse("Fail to add to new employee .")
        
        return redirect('retrieve_emp')
    else:
        return render(request, 'create_emp.html')

def retrieve_emp(request):
    employees_data = employees_info.objects.all()
    context = {'emp_all_data': employees_data}
    return render(request, 'retrieve_data.html', context)

def delete_emp(request, emp_id):
    new_emp = employees_info.objects.filter(id=emp_id).delete()
    return redirect('retrieve_emp')

def update_emp(request, emp_id):
    if request.method == 'POST':
        name = request.POST.get('emp_name')
        email = request.POST.get('emp_email')
        mob_no = request.POST.get('mob_no')
        employees_info.objects.filter(id=emp_id).update(name=name, email=email, Mob_no=mob_no)
        return redirect('retrieve_emp')
    else:
        employee = employees_info.objects.get(id=emp_id)
        context = {"update_emp_data": employee}
        return render(request, 'update.html', context)


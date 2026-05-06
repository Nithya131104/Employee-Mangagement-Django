from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .forms import Employee_Forms


def home(request):
    return HttpResponse("Hello Welcome To Employee Project")


def add(request):
    if request.method == "POST":
        employee_forms = Employee_Forms(request.POST)
        if employee_forms.is_valid():
            employee_forms.save()
    return render(request, 'Employee_Form.html', {'employee_forms': Employee_Forms})


def details(request):  # show details on ui
    return render(request, 'Employee_Details.html', {'all_detail': Employee.objects.all})


def emp_delete(request, id):  # delete employee
    employee_delete = Employee.objects.get(id=id)
    employee_delete.delete()
    return redirect('/details/')


def emp_update(request, id):  # update employee
    employee_update = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee_forms = Employee_Forms(request.POST, instance=employee_update)

        if employee_forms.is_valid():
            employee_forms.save()
            return redirect('/details/')

    return render(request, 'Employee_Form.html', {'employee_forms': Employee_Forms(instance=employee_update)})


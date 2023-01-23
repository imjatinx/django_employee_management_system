from django.shortcuts import render, HttpResponse, redirect
from django.http import request
from .models import Employee, Department, Role
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    employees = Employee.objects.all()
    context = {
        "emps": employees,
    }

    return render(request, 'all_emp.html', context)


def add_emp(request):
    Departments = Department.objects.all()
    Roles = Role.objects.all()

    context = {
        "depts": Departments,
        "roles": Roles
    }

    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']
        join_date = datetime.now()

        obj = Employee(first_name=first_name, last_name=last_name, dept_id=dept,
                       salary=salary, bonus=bonus, role_id=role, phone=phone, join_date=join_date)

        obj.save()

        return redirect('all_emp')

    return render(request, 'add_emp.html', context)


def remove_emp(request, emp_id):
    obj = Employee.objects.get(id=emp_id)
    obj.delete()
    return redirect('all_emp')


def filter_emp(request):
    return render(request, 'filter_emp.html')

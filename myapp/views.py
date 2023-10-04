from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def Demo(request):
    return render(request,'Home1.html')


def Adddemployee(request): 
    if request.method == 'POST':
        employeeId = request.POST.get('employeeId')
        fullName = request.POST.get('fullName')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        email = request.POST.get('email')
        company = request.POST.get('company')
        position = request.POST.get('position')
        salary=request.POST.get('salary')
        projects=request.POST.get('projects')
        employee=Employee(
                employeeId=employeeId,
                fullName=fullName,
                phone=phone,
                dob=dob,
                nationality=nationality,
                email=email,
                company=company,
                position=position,
                salary=salary,
                projects=projects,
        )
        employee.save()
        
       
    return render(request,'Registration.html')
                  

def Display(request):
    employees=Employee.objects.all()
    return render(request,"Display.html",{'employees':employees})



def delete(request, employee_id):
    employee = get_object_or_404(Employee, employeeId=employee_id)
    employee.delete()
    return redirect('Display')


def update(request, employee_id):
    employee = get_object_or_404(Employee, employeeId=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  
        if form.is_valid():
            form.save()
            return redirect('Display') 
    else:
        form = EmployeeForm(instance=employee)  

    return render(request, 'update_employee.html', {'form': form, 'employee': employee})


def view(request, employee_id):
    employee = get_object_or_404(Employee, employeeId=employee_id)
    return render(request, 'view_employee.html', {'employee': employee})
    

def search(request):
    query = request.GET.get('q')
    employees = Employee.objects.filter(fullName__icontains=query) if query else []
    return render(request, 'search.html', {'employees': employees, 'query': query})



def search(request):
    pro = request.GET.get('q')
    employees = Employee.objects.filter(projects__icontains=pro) if pro else []
    return render(request, 'searchbyproject.html', {'employees': employees, 'pro': pro})





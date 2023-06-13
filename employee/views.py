

# Create your views here.

# def index(request):
#     return render(request,'index.html')

from django.shortcuts import render
from .models import Employee

def create_employee(request):
    # Get the connection settings
    connection_settings = {
        'host': 'your_host',
        'username': 'your_username',
        'password': 'your_password',
        # Other connection settings
    }

    if request.method == 'POST':
        name = request.POST['name']
        identification = request.FILES['identification']
        # Process other form fields
        
        # Save the employee object
        employee = Employee(name=name, identification=identification)
        employee.save()
        
        return render(request, 'success.html', {'connection_settings': connection_settings})
    
    return render(request, 'form.html', {'connection_settings': connection_settings})
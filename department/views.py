from django.shortcuts import render
from .models import *

def create_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        # Process other form fields
        
        # Save the department object
        department = Department(name=name)
        department.save()
        
        return render(request, 'department/success.html')
    
    return render(request, 'department/form.html')

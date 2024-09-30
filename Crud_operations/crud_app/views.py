from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from crud_app.models import Employee,Department,Designation
from crud_app.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

# Create your views here.
@api_view(['GET'])
def display_data(request):
    objs = Employee.objects.all()
    serializer = EmployeeSerializer(objs,many=True)
    context = {'data':serializer.data}
    return render(request,"dis_data.html",context)


@api_view(['GET','POST'])
def create_data(request):
    departments = Department.objects.all()
    designations = Designation.objects.all()

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.info(request,'Successful')
            return redirect('/display')
        else:
            context = {
                'departments': departments,
                'designations': designations,
                'errors': serializer.errors,
            }
            messages.error(request,'Invalid Credentials')
            return render(request, "create_data.html", context)
    
    context = {
        'departments': departments,
        'designations': designations,
    }
    return render(request, "create_data.html", context)

@api_view(['GET', 'POST'])
def update_data(request, emp_id):
    try:
        employee = Employee.objects.get(pk=emp_id)
    except Employee.DoesNotExist:
        return render(request,"updated_data.html")

    if request.method == 'POST':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.info(request,'Updated Successful')
            return redirect('/display')
    else:
        serializer = EmployeeSerializer(employee)
        return render(request, 'updated_data.html', {'serializer': serializer})
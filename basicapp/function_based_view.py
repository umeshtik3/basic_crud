from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Employee
from .emp_serializer import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
import io


@csrf_exempt
def all_employee(request):
    if request.method == 'GET':
        all_employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(all_employees,many =True)
        json_data = JSONRenderer().render(employee_serializer.data)

        return HttpResponse(json_data,content_type= 'application/json')




@csrf_exempt
def get_employee(request,id):
    if request.method == 'GET':
        employee = Employee.objects.get(emp_id= id)
        employee_serializer = EmployeeSerializer(employee)
        json_data = JSONRenderer().render(employee_serializer.data)

        return HttpResponse(json_data,content_type= 'application/json')
    

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
     
        employee_serializer = EmployeeSerializer(data=python_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            all_employees = Employee.objects.all()
            employee_serializer = EmployeeSerializer(all_employees,many =True)
            json_data = JSONRenderer().render(employee_serializer.data)
            # json_data = JSONRenderer().render(employee_serializer.data)
        else:
            json_data = JSONRenderer().render(employee_serializer.error_messages)

        return HttpResponse(json_data,content_type= 'application/json')
    

import ast
from django.http import HttpResponse
from django.shortcuts import render
from basicapp.models import Employee
from django.db import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import json

def convert_byte_data_to_python_object(request_data):
  """Converts byte data from request to Python object.

  Args:
    request_data: The byte data from the request.

  Returns:
    The Python object converted from the byte data.
  """

  # Decode the byte data to a string.
  decoded_data = request_data.decode()

  # Try to parse the decoded data as JSON.
  # try:
  python_object = json.loads(decoded_data)
  # except json.JSONDecodeError:
    # If the decoded data is not valid JSON, try to parse it as a Python literal.
    # python_object = ast.literal_eval(decoded_data)

  return python_object


def convert_model_to_json_response(model) :
   json_data = {}
   for field in model._meta.fields :
      if isinstance(field, models.BigAutoField):
        json_data[field.name] = str(getattr(model, field.name))
      else:
        json_data[field.name] = getattr(model, field.name)
   
   return json.dumps(json_data)

@csrf_exempt
def employee(request):
    if request.method == 'GET':
        
        python_object = convert_byte_data_to_python_object(request.body)
        if len(python_object) == 0:
           all_employees = Employee.objects.all() # Select * from Employee 
           
           python_list = []
           for employee in all_employees:
              python_list.append({
                 "emp_id":employee.emp_id,
                 "name":employee.name,
                 "designation":employee.designation,
                 "department":employee.department,
              })
            
           json_response = json.dumps(python_list)
           return HttpResponse(json_response,content_type='application/json')


        else :
           employee_obj = Employee.objects.get(emp_id= python_object["emp_id"])
           json_response = convert_model_to_json_response(employee_obj)
            
        
           return HttpResponse(json_response,content_type='application/json')
    
       
       
    if request.method == 'POST':
        python_object = convert_byte_data_to_python_object(request.body)
        print(python_object)
        
        employeeObject = Employee(
         
           name = python_object["name"],
    designation = python_object["designation"],
    department = python_object["department"],
        )
        employeeObject.save()
        
        print(employeeObject.name)

        

        return HttpResponse()
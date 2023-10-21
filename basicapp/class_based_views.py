import io
from django.http import HttpResponse
from django.views import View
from .models import Employee
from .emp_serializer import EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

CONTENT_TYPE = 'application/json'


def convert_request_to_python_object(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    return python_data


def convert_into_json_data_and_render(serialize_data):
    return JSONRenderer().render(serialize_data)



@method_decorator(csrf_exempt, name="dispatch")
class EmployeeAPI(View):

    def get(self, request, *args, **kwargs):
       python_object = convert_request_to_python_object(request)

       emp_id = python_object.get('emp_id', None)

       if emp_id is not None:
           employee_obj = Employee.objects.get(emp_id = emp_id)
           employee_serializer = EmployeeSerializer(employee_obj)
           json_data = convert_into_json_data_and_render(employee_serializer.data)
           return HttpResponse(json_data,content_type = CONTENT_TYPE)
       

       employee_obj = Employee.objects.all()
       employee_serializer = EmployeeSerializer(employee_obj,many = True)
       json_data = convert_into_json_data_and_render(employee_serializer.data)
       return HttpResponse(json_data,content_type = CONTENT_TYPE)
       

    def post(self, request, *args, **kwargs):
        python_object = convert_request_to_python_object(request)
        employee_serializer = EmployeeSerializer(data=python_object)

        if employee_serializer.is_valid():
            employee_serializer.save()
            json_data = convert_into_json_data_and_render(employee_serializer.data)
            return HttpResponse(json_data,content_type = CONTENT_TYPE)
        else:
            json_data = convert_into_json_data_and_render(employee_serializer.errors)
            return HttpResponse(json_data,content_type = CONTENT_TYPE)
           

    def put(self, request, *args, **kwargs):
         python_object = convert_request_to_python_object(request)

         emp_id = python_object.get('emp_id')
         employee_obj = Employee.objects.get(emp_id = emp_id)
         employee_serializer = EmployeeSerializer(employee_obj, data=python_object,partial = True)
         if employee_serializer.is_valid():
            employee_serializer.save()
            json_data = convert_into_json_data_and_render(employee_serializer.data)
            return HttpResponse(json_data,content_type = CONTENT_TYPE)
         else:
            json_data = convert_into_json_data_and_render(employee_serializer.errors)
            return HttpResponse(json_data,content_type = CONTENT_TYPE)
       
   

    def delete(self,request,  *args, **kwargs):
        python_object = convert_request_to_python_object(request)
        emp_id = python_object.get('emp_id')
        employee_obj = Employee.objects.get(emp_id = emp_id)
        employee_obj.delete()

        response = {"status":"data has been deleted successfully."}
        json_data = convert_into_json_data_and_render(response)
        return HttpResponse(json_data,content_type = CONTENT_TYPE)



        







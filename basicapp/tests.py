from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
import json
from .models import Employee
from .emp_serializer import EmployeeSerializer

class EmployeeAPITests(TestCase):
    def setUp(self):
        self.employee_data = {
            'emp_id': 1,
            'name': 'John Doe',
            'designation': 'SDE',
            'department':'IT'
        }
        self.employee = Employee.objects.create(**self.employee_data)

    def test_get_all_employees(self):
        response = self.client.get(reverse('all-employees'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        expected_data = json.dumps(serializer.data, sort_keys=True)
        actual_data = json.dumps(json.loads(response.content), sort_keys=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(actual_data.encode(), expected_data.encode())
        

    def test_get_employee(self):
        response = self.client.get(reverse('get-employee', args=[self.employee.emp_id]))
        serializer = EmployeeSerializer(self.employee)
        expected_data = json.dumps(serializer.data, sort_keys=True)
        actual_data = json.dumps(json.loads(response.content), sort_keys=True)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(actual_data.encode(), expected_data.encode())

    def test_create_employee(self):
        new_employee_data = {
            'emp_id': 2,
            'name': 'Jane Smith',
            'designation': 'SDE',
            'department':'IT'
        }
        response = self.client.post(reverse('create-employee'), json.dumps(new_employee_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 2)

    def test_update_employee(self):
        updated_data = {
            'emp_id':2,
            'name': 'UPDATED NAME',
            'designation': 'Updated Developer',
            'department':'Updated IT',
           
        }
        response = self.client.put(reverse('update-employee', args=[self.employee.emp_id]), json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, updated_data['name'])
        self.assertEqual(self.employee.designation, updated_data['designation'])

    def test_delete_employee(self):
        response = self.client.delete(reverse('delete-employee', args=[self.employee.emp_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 0)

from rest_framework import serializers
from rest_framework.fields import empty
from basicapp.models import Employee


#custom fields in serializer
class CustomStringField(serializers.CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def run_validation(self, data):

        if not isinstance(data,str):
            raise serializers.ValidationError("Data Entered should be string type")
        
        data = data.upper()
        
        return super().run_validation(data)

class EmployeeSerializer(serializers.Serializer):
    emp_id = serializers.IntegerField()
    name = CustomStringField(max_length=100)
    designation = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    class Meta:
        model = Employee
        fields = "__all__"
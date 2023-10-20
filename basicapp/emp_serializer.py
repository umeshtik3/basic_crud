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
    
    def create(self,validated_data):
        """
        Create and return a new instance of YourModel, given the validated data.
        """
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.designation = validated_data.get("designation")
        instance.department = validated_data.get("department")
        instance.save()

        return instance
    
    
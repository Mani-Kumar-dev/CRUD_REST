from rest_framework import serializers
from crud_app.models import Department,Designation,Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department'] = instance.department.title
        representation['designation'] = instance.designation.title
        return representation
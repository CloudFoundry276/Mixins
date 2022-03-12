from rest_framework import serializers
from mixinsApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'exam_score']

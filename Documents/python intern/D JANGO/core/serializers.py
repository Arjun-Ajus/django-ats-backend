from rest_framework import serializers
from .models import JobUser, Job, Application

class JobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUser
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
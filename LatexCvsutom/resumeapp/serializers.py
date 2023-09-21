from rest_framework import serializers

class SkillJobTypeSerializer(serializers.Serializer):
    skills = serializers.ListField(child=serializers.CharField())
    job_type = serializers.CharField()
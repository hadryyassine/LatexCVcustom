from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SkillJobTypeSerializer

@api_view(['POST'])
def skill_job_type_endpoint(request):
    serializer = SkillJobTypeSerializer(data=request.data)
    if serializer.is_valid():
        skills = serializer.validated_data['skills']
        job_type = serializer.validated_data['job_type']
        
        # Process the data as needed
        # For example, modify the CV based on the skills and job type
        
        return Response({"message": "Data received successfully!"})
    return Response(serializer.errors, status=400)
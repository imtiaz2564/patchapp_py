from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SystemDataSerializer  # Import the serializer here


@api_view(['POST'])  # Get the data sent by the C# , Allow POST requests only
def receive_data(request):
    if request.method == 'POST':
        serializer = SystemDataSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, proceed with the logic
            validated_data = serializer.validated_data
            print(f"Received valid data: {validated_data}")

            # Respond with success and return the validated data
            return Response({"message": "Data received successfully", "received_data": validated_data},
                            status=status.HTTP_200_OK)
        else:
            # If the data is invalid, return an error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

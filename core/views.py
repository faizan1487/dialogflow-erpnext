from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['POST'])
def create_lead(request):
    data = request.data
    first_name = data.get('first_name')
    status = data.get('status')
    company = data.get('company')

    # Perform validation and error handling as needed

    # Make request to ERPNext API to create a new lead record
    erpnext_api_url = 'https://your_erpnext_instance/api/resource/Lead'
    erpnext_data = {
        'first_name': first_name,
        'status': status,
        'company': company
        # Add other fields as necessary
    }
    response = requests.post(erpnext_api_url, json=erpnext_data)

    if response.status_code == 200:
        return Response({'message': 'Lead created successfully'}, status=200)
    else:
        return Response({'error': 'Failed to create lead'}, status=500)

# dialogflow-erpnext
This is a middleware to connect dialogflow fulfillment webhook with erpnext lead doctype

## Django ERPNext Integration Project Overview

This Django project integrates with ERPNext to create lead records via RESTful API calls. It utilizes Django REST Framework for API views and communicates with ERPNext using HTTP requests.

## Requirements

Python 3.x  
Django  
Django REST Framework  
Requests library (for HTTP requests)


## Installation  
### 1-Clone the repository:

git clone https://github.com/faizan1487/dialogflow-erpnext.git


### 2-Install dependencies:

pip install -r requirements.txt



### 3-Run the project:

Copy code
python manage.py runserver

4-Post request to api endpoint from dialogflow fulfillment webhook

http://127.0.0.1:8000/core/api/create_lead/

Payload

{
    "first_name": "test user",
    "status": "test@",
    "company": "test company"
}

Usage  
Creating Lead Records: Send a POST request to /api/create_lead/ with JSON data containing lead information (e.g., {"first_name": "John", "status": "New", "company": "ABC Corp"}).
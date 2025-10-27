import requests

# URL of the running FastAPI server's predict endpoint
url = "http://127.0.0.1:8000/predict"

# Data to be sent for prediction
client_data = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

# Send a POST request and print the JSON response
response = requests.post(url, json=client_data)
print(response.json())
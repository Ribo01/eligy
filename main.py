import requests


sample_api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(sample_api_url)
print(f"Success:{response.status_code} for Eligy Test")


api_url = "https://jsonplaceholder.typicode.com/todos"
sample_data = {"userId": 1, "Firstname": "sadiq", "status": "test session"}
response = requests.post(api_url, json=sample_data)

print(f"Success:{response.status_code} for Eligy Test")
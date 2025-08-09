import json

file_path = r"p:\python\file\sample_data.json"
data = [
    {"name": "Rahim", "age": 25, "phone": "+880-123456789", "address": "Dhaka"},
    {"name": "Karim", "age": 30, "phone": "+880-987654321", "address": "Chittagong"}
    ]
with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)
    print("Data written to JSON file successfully!")

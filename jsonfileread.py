#এই কোড টিতে আমি চেস্টা করবো কিভাবে json ফাইল রিড ,ফাইলে  থেকে ডাটা নিতে হয় 
#
#
import json
data=[{}]
file_path = r"p:\python\file\sample_data.json"
with open(f"{file_path}",'r') as file:
    data=json.load(file)
search_name=input("Enter your name:").lower()
found = False
for user in data:
    if user['name'].lower() == search_name.lower():
        print(f"Found: {user['name']} {user['age']} {user['phone']} {user['address']}")
        found = True
        break

if not found:
    print("User not found.")
add_name=input("Name:").lower()
add_age=int(input("Age:"))
add_phone=int(input("Phone:"))
add_address=input("Address:")
data.append({
    "name":add_name,"age":add_age,"address":add_address,"phone":add_phone
})

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)
    print("Data written to JSON file successfully!")
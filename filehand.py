#this is my another file handeling system
#
#
#
import time
my_file_path=r"p:python\file\new.txt" #this is the location where create txt file
store_data=[]
with open(f"{my_file_path}",'r') as file:
    for text in file:
        name, age, address = text.strip().split(",", 2)  # প্রথম 2 কমার পর বাকিটা অ্যাড্রেস
        store_data.append({
            "name": name.strip(),
            "age": int(age.strip()),
            "address": address.strip()
        })
for data in store_data:
    print(data['age'])
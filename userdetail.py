#আমি এখানে ইউজার এর কিছু তথ্য ইনপুট নিব এবং এগুলো 
#
#
#
#file এ সেইভ করা
import os 
file_path=r"P:python\file\userdetail.txt"
user_details=[]# dictionary
print("Enter your details please:".title())
name=input("Name:")
age=int(input("Age:"))
mob="+880-"+input("Number:(without-+880)")
address=input("City:")
setlast="@example.com"
mail=input("Email:")
mail=mail+setlast
print("=====================")
user_details.append(
    {"Name":name,
    "Age":age,
    "Phone":mob,
    "Address":address,
    "mail":mail,
    }
)
with open(f"{file_path}",'a') as file:
    file.write("===============================\n")
    file.write("|       User Details save     |\n")
    file.write("===============================\n")
for res in user_details:
    print(f"Name:{res['Name']}")
    print(f"Age:{res['Age']}")
    print(f"Phone:{res['Phone']}")
    print(f"Address{res['Address']}")
    print(f"Email:{res['mail']}")
    with open(f"{file_path}",'a') as file:
        file.write(f"Name:{res['Name']}\n")
        file.write(f"Age:{res['Age']}\n")
        file.write(f"Phone:{res['Phone']}\n")
        file.write(f"Address:{res['Address']}\n")
        file.write(f"Email:{res['mail']}\n")
    
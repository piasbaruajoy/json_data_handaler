#ডাটা লোড করা
#ডাটা সার্চ করা
#নতুন ইউজার যোগ করা
#ডাটা ফাইলে সেভ করা
#সহজ মেনু দিয়ে ইউজার ইন্টারফেস
from colorama import Style,Fore
import time
settime=time.sleep(.5)
import json
name=None
age=None
phone=None
address=None

file_path=r"p:\python\file\sample_data.json"
with open(f"{file_path}",'r') as jasonfile:
    test=json.load(jasonfile)
def json_data():#json ফাইল থেকে ডাটা সো করাচ্ছি 
    print(Fore.LIGHTCYAN_EX+"==================================================================")
    print("|                "+Fore.YELLOW+"all json data list in jason file                "+Fore.LIGHTCYAN_EX+"|")
    print("==================================================================")

    for data in test:
        
        print(Fore.RED+f"|{data['name']:^15} "+Fore.LIGHTMAGENTA_EX+f"{data['age']:^10} "+Fore.LIGHTGREEN_EX+f"{data['phone']:^15} "+Fore.LIGHTWHITE_EX+f"{data['address']:^21}|")
        time.sleep(.5)
    print("==================================================================")
#নিজে এখন Json file থেকে নির্দিষ্ট ডাটা শো করার ফাংশন
def user_data_search():
    print(Fore.LIGHTGREEN_EX+"==================================================================")
    print("|               "+Fore.WHITE+"Find specific data from jason file                "+Fore.LIGHTCYAN_EX+"|")
    print("==================================================================")
    
    while True:
        search_by_name=input("    "+Fore.YELLOW+"Enter Name For searching Data from Json FIle:")
        print(Fore.LIGHTCYAN_EX+"==================================================================")
        check=False
        for data in test:
            
            if data['name'].lower() == search_by_name.lower():
                print("|    "+Fore.LIGHTGREEN_EX+"FULL NAME   |"+Fore.RED+"   AGE  |"+Fore.YELLOW+"    CONTRACT NUMBER  |"+Fore.LIGHTBLUE_EX+"     LOCATION   |")
                print(Fore.LIGHTCYAN_EX+"==================================================================")
                print(f"|"+Fore.LIGHTGREEN_EX+f"{data['name']:^15} | "+Fore.RED+f"{data['age']:^7}|"+Fore.YELLOW+f" {data['phone']:^20}| "+Fore.LIGHTBLUE_EX+f"{data['address']:^15}|")
                time.sleep(.5)
                print(Fore.LIGHTCYAN_EX+"==================================================================")
                check=True
                break

        if check:
            break
        else:
            print(Fore.Red+"   No data found please search another name\n".title())

# এখন নতুন  ডাটা ইন্সারট করা 
def insert_new_data_in_json():
    print(Fore.LIGHTGREEN_EX+"==================================================================")
    print("|                 "+Fore.LIGHTMAGENTA_EX+"Adding new  data in jason file                 "+Fore.LIGHTGREEN_EX+"|")
    print("==================================================================")
    name=input(Fore.BLUE+"Enter Name:").capitalize()
    age=int(input(Fore.RED+"Enter Age:"))
    phone=input(Fore.YELLOW+"Enter Phone Number without(+880):")
    phone="+880-"+phone
    address=input(Fore.CYAN+"Enter Address:")
    test.append({
    "name":name,"age":age,"address":address,"phone":phone
})
    with open(file_path,'w') as f:
        json.dump(test, f, indent=4)
        print(Fore.GREEN+"Data written to JSON file successfully!")
#মুডিফাই ডাটা নিদিষ্ট Json file এর ইনফরমেশন থেকে
def modifying_data():
    print(Fore.LIGHTGREEN_EX+"==================================================================")
    print(Fore.LIGHTGREEN_EX+"|                "+Fore.RED+"all json data list in jason file                "+Fore.LIGHTGREEN_EX+"|")
    print("==================================================================")
    print("|    "+Fore.LIGHTGREEN_EX+"FULL NAME   |"+Fore.RED+"   AGE  |"+Fore.YELLOW+"    CONTRACT NUMBER  |"+Fore.LIGHTBLUE_EX+"     LOCATION   |")
    print(Fore.LIGHTGREEN_EX+"==================================================================")
    for data in test:
        print(Fore.LIGHTGREEN_EX+f"|"+Fore.LIGHTGREEN_EX+f"{data['name']:^15} | "+Fore.RED+f"{data['age']:^7}|"+Fore.YELLOW+f" {data['phone']:^20}| "+Fore.LIGHTBLUE_EX+f"{data['address']:^15}"+Fore.LIGHTGREEN_EX+"|")
    print("==================================================================")
    mode_data=input("whichi user data you want to modify?")
    for data in test:
        if data['name'].lower() == mode_data.lower():
            print(Fore.WHITE+"1.For Update Name:")
            print("2.For Update Age")
            print("3.For Update Number")
            print("4.For Update Address")
            value=int(input(Fore.CYAN+"Your Choise(1-4)"))
            if(value==1):
                name=input("Enter your Real Name for Updating:").lower()
                data['name']=name
            elif(value==2):
                age=int(input("Enter your Current Age for Updateing:"))
                data['age']=age
            elif(value==3):
                phone=input("Enter your Current Phone number for Updating:").lower()
                data['phone']=phone
            elif(value==4):
                address=(input("Enter your Current Address for Updateing:"))
                data['address']=address
            else:
                print("Wrong Choise")
            with open(file_path,'w') as f:
                json.dump(test, f, indent=4)
                print(Fore.GREEN+"Data written to JSON file successfully!")
                break
    
def main():#সহজ মেনু দিয়ে ইউজার ইন্টারফেস
    choice=None
   
    while choice!=5:
        print()
        print()
        print()
        print(Fore.LIGHTBLUE_EX+"=======================================")
        print("|     "+Fore.LIGHTGREEN_EX+"Json File and data handling      "+Fore.LIGHTBLUE_EX+"|")    
        print("=======================================")
        print("|"+Fore.CYAN+"1.see all existing data on json file  "+Fore.LIGHTBLUE_EX+"|")
        print("|"+Fore.YELLOW+"2.search specific data form json file "+Fore.LIGHTBLUE_EX+"|")
        print("|"+Fore.RED+"3.Insert new data in json file        "+Fore.LIGHTBLUE_EX+"|")
        print("|"+Fore.MAGENTA+"4.Modify existing data form json file "+Fore.LIGHTBLUE_EX+"|")
        print("|"+Fore.LIGHTGREEN_EX+"5.Exit form the program               "+Fore.LIGHTBLUE_EX+"|")
        print("=======================================",end=Fore.RESET+"\n")
        print()
        print()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
            continue
        if(choice==1):
            json_data()
        elif(choice==2):
            user_data_search()
        elif(choice==3):
            insert_new_data_in_json()
        elif(choice==4):
            modifying_data()
        elif(choice==5):
            print("you click 5 ")  
            exit()
        else:
            print("Invalid choice! Please enter 1 to 5.")
            continue
if __name__ == "__main__":
    main()
# now i am going to write a code how to use txt file as a data
#
#fist store some data on a txt file 
#
# for work purpose i alreday store some information in a txt file 
#
#so first read the information
#
#
import time
from colorama import Style,Fore
file_path=r"p:python\file\new.txt"
my_storage=[]
with open(f"{file_path}","r") as file:# so new file is opened 
    for text in file:
        name,age,address=text.strip().split(",",2) #use strip for \n and split(",",2) for address
        my_storage.append({
            "name":name.strip(),
            "age": int(age.strip()),
            'address':address.strip()
        })
#print(my_storage)
print(" =========================================================")
print("|   "+Fore.YELLOW+"Full Name      |"+Fore.GREEN+"  age   |"+Fore.MAGENTA+"            address         |",end=Style.RESET_ALL+"\n")
print(" =========================================================")
for x in my_storage:
    print(f"|"+Fore.RED+f"{x['name']:^18}|"+Fore.CYAN+f"{x['age']:^8}|"+Fore.BLUE+f"{x['address']:^28}|",end=Style.RESET_ALL+"\n")
    time.sleep(.5)
print(" =========================================================")
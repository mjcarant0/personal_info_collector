#Use dictionary to store user's personal information
personal_info = {}
#Use while loop to collect information
while True:
    try:
        name = input("Name: ")
        age = int(input("Age: "))
        birthday = input("Birthday: ")
        sex = input("Sex: ")
        phone_number = int(input("Phone Number: "))
        address = input("Address: ")
        email_account = input("Email account: ")
        
        personal_info[name] = {
            'name': name,
            'age': age,
            'birthday': birthday,
            'sex': sex,
            'phone_number': phone_number,
            'address': address,
            'email_account': email_account
        }
        
        print(f"Your information: {personal_info[name]}")
        
        add_new_info = input("Do you want to add new information? YES or NO: ").upper()
        
    except:
        print("Invalid Input")
    
    if add_new_info == "YES":
        continue
    elif add_new_info == "NO":
        break
    else:
        print("Invalid Input")
#Add information in personal_info_collector.txt file

#Print user information
print(personal_info)
#Ask user if they want to add another personal information

#Print all information if they answer "no"
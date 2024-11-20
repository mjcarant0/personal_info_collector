import re #condition for name

#Use dictionary to store user's personal information
personal_info = {}
#Use while loop to collect information
while True:
    try:
        while True: #loop and condition for name
            name = input("Name: ")
            
            if not re.match(r"^[A-Za-z\s'-.]+$", name): 
                print("Invalid name. Please try again.")
            else: 
                break
        
        while True:
            age = int(input("Age: "))
            
            if age >= 0:
                break
            else:
                print("Age must be a non-negative number.")
        
        birthday = input("Birthday: ")
        
        
        sex = input("Sex. Enter M if you are male, and F if you are female: ").upper()
        
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
        
        #Print user information
        print("-----------------------------------------------------------")
        print("This is your personal information")
        print(f"Name: {personal_info[name]['name']}")
        print(f"Age: {personal_info[name]['age']}")
        print(f"Birthday: {personal_info[name]['birthday']}")
        print(f"Sex: {personal_info[name]['sex']}")
        print(f"Phone Number: {personal_info[name]['phone_number']}")
        print(f"Address: {personal_info[name]['address']}")
        print(f"Email Account: {personal_info[name]['email_account']}")
        print("-----------------------------------------------------------")
        
        
        #Ask user if they want to add another personal information
        add_new_info = input("Do you want to add new information? YES or NO: ").upper()
        
        if add_new_info == "YES":
            continue
        elif add_new_info == "NO":
            break
        else:
            print("Invalid Input")
        
    except:
        print("Invalid Input")
    
    
#Add information in personal_info_collector.txt file

#Print all information if they answer "no"
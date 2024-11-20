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
        
        while True: #loop and condition for age
            age = int(input("Age: "))
            
            if age >= 0:
                break
            else:
                print("Age must be a non-negative number.")
        
        while True: #loop and condition for birthday
            print("Birthday")
            
            while True:
                month = input("Month: ").capitalize()
                
                valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                
                if month in valid_months:
                    break
                else:
                    print("Invalid Month. Please try again.")
            
            while True:
                day = int(input("Day: "))
                
                if day >= 1 and day <= 31:
                    break
                else:
                    print("Invalid day. Please try again.")
                    
            while True:
                year = int(input("Year: "))
                
                if year >= 1000 and year <= 2024:
                    break
                else:
                    print("Invalid Year. Please try again.")
            
            birthday = f"{month} {day}, {year}"
            
            print(f"Birthday: {birthday}")
            break
        
        while True: #loop and condition for sex
            sex = input("Sex. Enter M if you are male, and F if you are female: ").upper()
            
            if sex == "M":
                sex = "Male"
                break
            elif sex == "F":
                sex = "Female"
                break
            else:
                print("Invalid sex. Please try again.")
        
        while True: #loop and condition for address
            print("Address")
            
            address_line = input("Address Line: ")
            country = input("Country: ").capitalize()
            
            address = f"{address_line}, {country}"
            print(f"Address: {address}")
            break
            
        email_account = input("Email account: ")
        
        while True: #loop and condition for marital status
            marital_status = input("Marital Status (Single, Married, Divorced, Separated, or Widowed): ").capitalize()

            valid_status = ['Single', 'Married', 'Divorced', 'Separated', 'Widow']
            
            if marital_status in valid_status:
                break
            else:
                print("Invalid Marital Status. Please try again.")
                
        personal_info[name] = {
            'name': name,
            'age': age,
            'birthday': birthday,
            'sex': sex,
            'address': address,
            'email_account': email_account,
            'marital_status': marital_status
        }
        
        #Print user information
        print("-----------------------------------------------------------")
        print("This is your personal information")
        print(f"Name: {personal_info[name]['name']}")
        print(f"Age: {personal_info[name]['age']}")
        print(f"Birthday: {personal_info[name]['birthday']}")
        print(f"Sex: {personal_info[name]['sex']}")
        print(f"Address: {personal_info[name]['address']}")
        print(f"Email Account: {personal_info[name]['email_account']}")
        print(f"Marital Status: {personal_info[name]['marital_status']}")
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
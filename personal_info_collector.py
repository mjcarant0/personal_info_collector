import re #condition for name and email
import os

#File path for the .txt file
os.chdir(r'D:\BSCpE\PLD\Individual\personal_info_collector') 
file_path = r'D:\BSCpE\PLD\Individual\personal_info_collector\personal_info.txt'

#Use dictionary to store user's personal information
personal_info = {}
#Use while loop to collect information
while True:
    try:
        while True: #loop and condition for username
            username = input("Enter your username (at least 5 characters): ")
            
            if len(username) >= 5:
                if username in personal_info:
                    print("Username already exists. Please choose a different username.")
                else:
                    break
            else:
                print("Username must be at least 5 characters. Please try again.")
                
        while True: #loop and condition for password
            password = input("Password (at least 8 characters): ")
            
            if len(password) >= 8:
                break
            else:
                print("Password must be at least 8 characters. Please try again.")
        
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
                
                if year >= 1800 and year <= 2024:
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
        
        while True: #loop and condition for email account    
            email_account = input("Email account: ")
            email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if re.match(email, email_account):
                break
            else:
                print("Invalid Email Account. Please try again.")
        
        while True: #loop and condition for marital status
            marital_status = input("Marital Status (Single, Married, Divorced, Separated, or Widowed): ").capitalize()

            valid_status = ['Single', 'Married', 'Divorced', 'Separated', 'Widow']
            
            if marital_status in valid_status:
                break
            else:
                print("Invalid Marital Status. Please try again.")
                
        personal_info[username] = {
            'username': username,
            'password': password,
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
        print(f"Username: {personal_info[username]['username']}")
        print(f"Password: {personal_info[username]['password']}")
        print(f"Name: {personal_info[username]['name']}")
        print(f"Age: {personal_info[username]['age']}")
        print(f"Birthday: {personal_info[username]['birthday']}")
        print(f"Sex: {personal_info[username]['sex']}")
        print(f"Address: {personal_info[username]['address']}")
        print(f"Email Account: {personal_info[username]['email_account']}")
        print(f"Name: {personal_info[username]['name']}")
        print(f"Marital Status: {personal_info[username]['marital_status']}")
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
    
    
#Add information in personal_info.txt file
if add_new_info == "NO":
    with open(file_path, "a") as file:
        file.write("All collected personal information:\n")
        file.write("-----------------------------------------------------------\n")
        for name, info in personal_info.items():
            file.write(f"Username: {info['username']}\n")
            file.write(f"Password: {info['password']}\n")
            file.write(f"Name: {info['name']}\n")
            file.write(f"Age: {info['age']}\n")
            file.write(f"Birthday: {info['birthday']}\n")
            file.write(f"Sex: {info['sex']}\n")
            file.write(f"Address: {info['address']}\n")
            file.write(f"Email Account: {info['email_account']}\n")
            file.write(f"Marital Status: {info['marital_status']}\n")
            file.write("-----------------------------------------------------------\n")

#Print all information if they answer "no"
    print("-----------------------------------------------------------")
    print("All collected personal information")
    for name, info in personal_info.items():
        print(f"Username: {personal_info[username]['username']}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Birthday: {info['birthday']}")
        print(f"Sex: {info['sex']}")
        print(f"Address: {info['address']}")
        print(f"Email Account: {info['email_account']}")
        print(f"Marital Status: {info['marital_status']}")
        print("-----------------------------------------------------------")
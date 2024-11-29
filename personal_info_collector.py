import re #condition for name and email
import os
import colorama #adding color for text
from colorama import Fore, Back, Style

#File path for the .txt file
os.chdir(r'D:\BSCpE\PLD\Individual\personal_info_collector') 
file_path = r'D:\BSCpE\PLD\Individual\personal_info_collector\personal_info.txt'

#Use dictionary to store user's personal information
personal_info = {}
#Use while loop to collect information
while True:
    while True:
        try:
            while True: #loop and condition for username
                username = input(f"{Fore.YELLOW}Enter your username (at least 5 characters): {Style.RESET_ALL}")
                
                if len(username) >= 5:
                    if username in personal_info:
                        print(f"{Back.RED}{Style.BRIGHT} Username already exists. Please choose a different username. {Style.RESET_ALL}")
                    else:
                        break
                else:
                    print(f"{Back.RED}{Style.BRIGHT}Username must be at least 5 characters. Please try again. {Style.RESET_ALL}")
                    
            while True: #loop and condition for password
                password = input(f"{Fore.YELLOW}Password (at least 8 characters): {Style.RESET_ALL}")
                
                if len(password) >= 8:
                    break
                else:
                    print(f"{Back.RED}{Style.BRIGHT} Password must be at least 8 characters. Please try again. {Style.RESET_ALL}")
            
            while True: #loop and condition for name
                name = input(f"{Fore.YELLOW}Name: {Style.RESET_ALL}")
                
                if not re.match(r"^[A-Za-z\s'-.]+$", name): 
                    print(f"{Back.RED}{Style.BRIGHT} Invalid name. Please try again. {Style.RESET_ALL}")
                else: 
                    break
            
            while True: #loop and condition for age
                age_input = input(f"{Fore.YELLOW}Age: {Style.RESET_ALL}")
                
                try:
                    age = int(age_input)
                    if age >= 0:
                        break
                    else:
                        print(f"{Back.RED}{Style.BRIGHT} Age must be a non-negative number. {Style.RESET_ALL}")
                except ValueError:
                    print(f"{Back.RED}{Style.BRIGHT} Invalid age input. Please enter a valid number. {Style.RESET_ALL}")
                    
            while True: #loop and condition for birthday
                print(f"{Fore.YELLOW}Birthday{Style.RESET_ALL}")
                
                while True:
                    month = input(f"{Fore.YELLOW}Month: {Style.RESET_ALL}").capitalize()
                    
                    valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                    
                    if month in valid_months:
                        break
                    else:
                        print(f"{Back.RED}{Style.BRIGHT} Invalid Month. Please try again. {Style.RESET_ALL}")
                
                while True:
                    day = int(input(f"{Fore.YELLOW}Day: {Style.RESET_ALL}"))
                    
                    if day >= 1 and day <= 31:
                        break
                    else:
                        print(f"{Back.RED}{Style.BRIGHT} Invalid day. Please try again. {Style.RESET_ALL}")
                        
                while True:
                    year = int(input(f"{Fore.YELLOW}Year: {Style.RESET_ALL}"))
                    
                    if year >= 1800 and year <= 2024:
                        break
                    else:
                        print(f"{Back.RED}{Style.BRIGHT} Invalid Year. Please try again. {Style.RESET_ALL}")
                
                birthday = f"{month} {day}, {year}"
                
                print(f"{Fore.YELLOW}Birthday:{Style.RESET_ALL} {birthday}")
                break
            
            while True: #loop and condition for sex
                sex = input(f"{Fore.YELLOW}Sex. Enter M if you are male, and F if you are female: {Style.RESET_ALL}").upper()
                
                if sex == "M":
                    sex = "Male"
                    break
                elif sex == "F":
                    sex = "Female"
                    break
                else:
                    print(f"{Back.RED}{Style.BRIGHT} Invalid sex. Please try again. {Style.RESET_ALL}")
            
            while True: #loop and condition for address
                print(f"{Fore.YELLOW}Address{Style.RESET_ALL}")
                
                address_line = input(f"{Fore.YELLOW}Address Line: {Style.RESET_ALL}")
                country = input(f"{Fore.YELLOW}Country: {Style.RESET_ALL}")
                
                address = f"{address_line}, {country}"
                print(f"{Fore.YELLOW}Address: {Style.RESET_ALL}{address}")
                break
            
            while True: #loop and condition for email account    
                email_account = input(f"{Fore.YELLOW}Email account: {Style.RESET_ALL}")
                email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                
                if re.match(email, email_account):
                    break
                else:
                    print(f"{Back.RED}{Style.BRIGHT} Invalid Email Account. Please try again. {Style.RESET_ALL}")
            
            while True: #loop and condition for marital status
                marital_status = input(f"{Fore.YELLOW}Marital Status (Single, Married, Divorced, Separated, or Widowed): {Style.RESET_ALL}").capitalize()

                valid_status = ['Single', 'Married', 'Divorced', 'Separated', 'Widow']
                
                if marital_status in valid_status:
                    break
                else:
                    print(f"{Back.RED}{Style.BRIGHT} Invalid Marital Status. Please try again. {Style.RESET_ALL}")
                    
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
            print(f"{Style.BRIGHT}{Back.CYAN} All collected personal information {Style.RESET_ALL}")
            print(f"Username: {personal_info[username]['username']}")
            print(f"Password: {personal_info[username]['password']}")
            print(f"Name: {personal_info[username]['name']}")
            print(f"Age: {personal_info[username]['age']}")
            print(f"Birthday: {personal_info[username]['birthday']}")
            print(f"Sex: {personal_info[username]['sex']}")
            print(f"Address: {personal_info[username]['address']}")
            print(f"Email Account: {personal_info[username]['email_account']}")
            print(f"Marital Status: {personal_info[username]['marital_status']}")
            print("-----------------------------------------------------------")
            
            #ask user if they want to add new info
            while True:
                add_new_info = input(f"{Fore.CYAN} Do you want to add new information? YES or NO: {Style.RESET_ALL}").upper()
                
                #condition for new info
                if add_new_info == "YES":
                    break
                elif add_new_info == "NO":
                    #Add information in personal_info.txt file
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
                    break
                else:
                    print(f"{Back.RED}{Style.BRIGHT} Invalid Input. Please enter YES or NO. {Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Back.RED}{Style.BRIGHT} Invalid Input. {Style.RESET_ALL} Error: {e}")
    
    
    if add_new_info == "NO":
        #Print all information if they answer "no"
        print("-----------------------------------------------------------")
        print(f"{Style.BRIGHT}{Back.CYAN} All collected personal information {Style.RESET_ALL}")
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
        break
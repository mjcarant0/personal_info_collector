import colorama #adding color for text
from colorama import Fore, Back, Style

file_path = r'D:\BSCpE\PLD\Individual\personal_info_collector\personal_info.txt' #file path for personal_info.txt file

personal_info = {} #empty dictionary to store info from .txt file

#Read all personal information in personal_info.txt and store into dictionary
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        user_info = {}
        for line in lines:
            if line in lines:
                #skip the separator lines
                if line.strip() == "-----------------------------------------------------------":
                    if user_info:  #Save last user info before starting a new one
                        personal_info[user_info['username']] = user_info
                    user_info = {}
                    continue
                line = line.strip()
                if line.startswith("Username:"):
                    user_info['username'] = line.split(":")[1].strip()
                elif line.startswith("Password:"):
                    user_info['password'] = line.split(":")[1].strip()
                elif line.startswith("Name:"):
                    user_info['name'] = line.split(":")[1].strip()
                elif line.startswith("Age:"):
                    user_info['age'] = line.split(":")[1].strip()
                elif line.startswith("Birthday:"):
                    user_info['birthday'] = line.split(":")[1].strip()
                elif line.startswith("Sex:"):
                    user_info['sex'] = line.split(":")[1].strip()
                elif line.startswith("Address:"):
                    user_info['address'] = line.split(":")[1].strip()
                elif line.startswith("Email Account:"):
                    user_info['email_account'] = line.split(":")[1].strip()
                elif line.startswith("Marital Status:"):
                    user_info['marital_status'] = line.split(":")[1].strip()
                    
        #Ensure the last user is added after the loop finishes
        if user_info:
            personal_info[user_info['username']] = user_info
        
except:
    print(f"{Back.RED}{Style.BRIGHT}An error occurred.{Style.RESET_ALL}")

if len(personal_info) > 0: #condition to check if the dictionary contains information
    #New loop to ask the user to input their username and password
    while True:
        try:
        #Ask user to input their username
            username = input(f"{Fore.YELLOW}Enter your username: {Style.RESET_ALL}")
        #Ask user to input their password
            password = input(f"{Fore.YELLOW}Enter your password: {Style.RESET_ALL}")
        #If user's username and password in personal_info.txt, print their personal information
            if username in personal_info and personal_info[username]['password'] == password:
                user_info = personal_info[username]
                print(f"{Style.BRIGHT}{Back.CYAN}\nUser Information{Style.RESET_ALL}")
                print(f"Username: {user_info['username']}")
                print(f"Name: {user_info['name']}")
                print(f"Age: {user_info['age']}")
                print(f"Birthday: {user_info['birthday']}")
                print(f"Sex: {user_info['sex']}")
                print(f"Address: {user_info['address']}")
                print(f"Email Account: {user_info['email_account']}")
                print(f"Marital Status: {user_info['marital_status']}")
            else:
                print(f"{Back.RED}{Style.BRIGHT}Username or Password is incorrect. Try again.{Style.RESET_ALL}")
            
            #Ask user if they want to check other information
            while True:
                print("-----------------------------------------------------------")
                user_checking = input(f"{Fore.CYAN}Do you want to check another user? (YES/NO): {Style.RESET_ALL}").upper()
                
                if user_checking == "YES":
                    print("-----------------------------------------------------------")
                    break
                elif user_checking == "NO":
                    print(f"{Fore.RED}Exiting the program...{Style.RESET_ALL}")
                    exit()
                else:
                    (f"{Back.RED}{Style.BRIGHT}Invalid input. Please input 'YES' or 'NO'.{Style.RESET_ALL}")

        except Exception as e:
            # Handle general exceptions
            print(f"{Back.RED}{Style.BRIGHT}An error occurred: {e} {Style.RESET_ALL}")

else: #if there is no information
    print(f"{Back.RED}{Style.BRIGHT}No user information found. Exiting the program...{Style.RESET_ALL}")
file_path = r'D:\BSCpE\PLD\Individual\personal_info_collector\personal_info.txt' #file path for personal_info.txt file

personal_info = {} #empty dictionary to store info from .txt file

#Read all personal information in personal_info.txt and store into dictionary
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        user_info = {}
except:
    print("An error occurred.")

while True:
    try:
    #Ask user to input their username
        username = input("Enter your username: ")
    #Ask user to input their password
        password = input("Enter your password: ")
    #If user's username and password in personal_info.txt, print their personal information
        if username in personal_info and personal_info[username]['password'] == password:
            user_info = personal_info[username]
            print("\nUser Information:")
            print(f"Username: {user_info['username']}")
            print(f"Name: {user_info['name']}")
            print(f"Age: {user_info['age']}")
            print(f"Birthday: {user_info['birthday']}")
            print(f"Sex: {user_info['sex']}")
            print(f"Address: {user_info['address']}")
            print(f"Email Account: {user_info['email_account']}")
            print(f"Marital Status: {user_info['marital_status']}")
        else:
            print("Username or Password is incorrect. Try again.")
    #Ask user if they want to check other information

    except:
        print("Invalid input. Try again.")
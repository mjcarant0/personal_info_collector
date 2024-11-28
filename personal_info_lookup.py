file_path = r'D:\BSCpE\PLD\Individual\personal_info_collector\personal_info.txt'

personal_info = {}

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
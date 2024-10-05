from cryptography.fernet import Fernet

#comment this after generating the key once and save it to a file
'''def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

#write_key()  #run this only once

key = load_key()  # Use the key directly
fer = Fernet(key)  # Correct capitalization

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User: ", user, "| Password: ",
                 fer.decrypt(pwd.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press Q to quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")

from cryptography. fernet import Fernet



key = " passwordmanager"

def load_key():
    return open("key.key", "rb").read()

'''
key = key.encode()
fernet = Fernet(key)
'''


master_pwd = input("What is the master password? ")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("Account Name:", user, "| Password:", pwd)
while True:
    mode = input("Would you like to add a new password or view existing ones (view/add)? Press q to quit. ").lower()
    if mode == "q":
        break

    elif mode == "add":
        add()   


    elif mode == "view":
        view()

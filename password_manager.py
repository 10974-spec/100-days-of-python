from nt import read


master_pwd = input("what is the master password? ")

def view():
      with open('passwords.txt', 'f') as f:   #r-read, w-write, a-append
        for line in f.readlines():
            print(line)
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:   #r-read, w-write, a-append
        f.write(name + "|" + pwd + "\n")
      
        
while True:
    mode = input("Do you want to add a new password or view existing ones (view/add), press q to quit? ").lower()
    if mode == "q":
        break
        
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        quit()
  
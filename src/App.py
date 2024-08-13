try:
    from src.Encryption import Encryption
    from os import system, name
    from os.path import exists
    from getpass import getpass
    from pyperclip import copy
except:
    raise ImportError("Import of modules failed")

clear = lambda: system('cls' if name == 'nt' else 'clear')
wait = lambda: input("Press enter to continue...")

class App:
    def __init__(self, filePath, password: str) -> None:
        self.filePath = filePath
        self.password = password
        if ((filePath == None) or (self.fileExist() == False) or (self.password == None)):
            self.mainMenu()
        
        self.initEncryption()
        
        try:
            self.data = self.encryption.decrypt()

        except ValueError as e:
            print(f"[!] ValueError: {e}")
            print(f"[!] Verify your password")
            exit(2)
        
        self.run()
    
    def mainMenu(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        
        print("1. Open password file\n2. Create password file\n3. Exit")
        answer = input("What do you want to do? ")
        
        match int(answer):
            case 1:
                self.filePath = input("Enter the file path: ")
                if (self.fileExist() == False):
                    self.mainMenu()
                else:
                    self.password = getpass("Enter the file password: ")
            
            case 2:
                self.filePath = input("Enter the directory for the file: ")
                if (self.fileExist() == False):
                    print("this directory doesn't exist.")
                    wait()
                    self.mainMenu()
                else:
                    self.filePath += "\\" + input("Enter a name for your password file: ")
                    self.password = getpass("Enter the file password: ")
                
                self.initEncryption()
                self.encryption.encrypt({"passwords": []})

            case 2:
                raise NotImplementedError("Create password file")
            
            case 3:
                exit(0)

    def run(self):
        isRunning = True
        
        while isRunning:
            clear()
            print("     Password Manager\n    ------------------\n")
            
            print("1. Print passwords\n2. Add password\n3. Delete password\n4. Copy password\n5. Exit")
            answer = input("What do you want to do? ")
            
            match int(answer):
                case 1:
                    self.printPasswords()
                
                case 2:
                    self.addPassword()
                
                case 3:
                    self.deletePassword()
                
                case 4:
                    self.copyPassword()
                
                case 5:
                    isRunning = False
    
    def printPasswords(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        print("Passwords: ")
        for password in self.data["passwords"]:
            print(f"{password["title"]} | {password["username"]} : {password["password"]}")
            
        wait()
    
    def addPassword(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        title = input("Enter the title: ")
        username = input("Enter the user name: ")
        password = getpass("Enter the password: ")
        self.data["passwords"].append({"title": title, "username": username, "password": password})
        self.encryption.encrypt(self.data)
    
    def deletePassword(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        title = input("Enter the password title: ")
        
        find = False
        for password in self.data["passwords"]:
            if password["title"] == title:
                self.data["passwords"].remove(password)
                self.encryption.encrypt(self.data)
                find = True
        
        if find == False:
            print("This password doesn't exist.")
            wait()
    
    def copyPassword(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        title = input("Enter the password title: ")
        
        find = False
        for password in self.data["passwords"]:
            if password["title"] == title:
                copy(password["username"])
                print("User name has been copied")
                wait()
                copy(password["password"])
                print("Password has been copied")
                wait()
                find = True
        
        if find == False:
            print("This password doesn't exist")
            wait()
    
    def initEncryption(self):
        self.encryption = Encryption(filePath=self.filePath, password=self.password)
    
    def fileExist(self) -> bool:
        if (exists(self.filePath)):
            return True

        return False
try:
    from Encryption import Encryption
    from os import system, name
    from os.path import exists
    from getpass import getpass
except:
    raise ImportError("Import of modules failed")

clear = lambda: system('cls' if name == 'nt' else 'clear')

class App:
    def __init__(self, filePath, password: str) -> None:
        self.filePath = filePath
        self.password = password
        if ((filePath == None) or (self.fileExist() == False) or (self.password == None)):
            self.mainMenu()
        
        encryption = Encryption(filePath=self.filePath, password=self.password)
        try:
            self.data = encryption.decrypt()

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
                    raise NotImplementedError("Add password method")
                
                case 3:
                    raise NotImplementedError("Delete password method")
                
                case 4:
                    raise NotImplementedError("Copy password method")
                
                case 5:
                    isRunning = False
    
    def printPasswords(self) -> None:
        clear()
        print("     Password Manager\n    ------------------\n")
        print("Passwords: ")
        for password in self.data["passwords"]:
            print(f"{password["title"]} | {password["username"]} : {password["password"]}")
            
        input("Press enter to continue...")
    
    def fileExist(self) -> bool:
        if (exists(self.filePath)):
            return True

        return False
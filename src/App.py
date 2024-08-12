try:
    from json import load
    from Encryption import Encryption
    from os.path import exists
except:
    raise ImportError("Import of modules failed")

class App:
    def __init__(self, filePath, password: str) -> None:
        self.filePath = filePath
        if ((filePath == None) or (self.fileExist() == False)):
            self.mainMenu()
        
        encryption = Encryption(filePath=self.filePath, password=password)
        self.data = encryption.decrypt()
    
    def mainMenu(self):
        print("     Password Manager\n    ------------------\n")
        
        print("1. Open password file\n2. Create password file\n3. Exit")
        answer = input("What do you want to do? ")
        
        match int(answer):
            case 1:
                self.filePath = input("Enter the file path: ")
                if (self.fileExist() == False):
                    self.mainMenu()

            case 2:
                raise NotImplementedError("Create password file")
            
            case 3:
                exit(0)

    def run(self):
        print("     Password Manager\n    ------------------\n")
        
        print("1. Read file\n5. Exit")
        answer = input("What do you want to do? ")
        
        match int(answer):
            case 1:
                print(self.data)
            
            case 5:
                exit(0)
    
    def fileExist(self) -> bool:
        if (exists(self.filePath)):
            return True

        return False
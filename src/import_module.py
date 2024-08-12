try:
    from subprocess import run
    from importlib import import_module
    from os import system
    from time import sleep
except:
    raise ImportError("Import of modules failed")

clear = lambda: system('cls')

def check_installation(module_name):
    try:
        import_module(module_name)
        
    except ImportError:
        print(f"{module_name} is not installed. Installing in progress...")
        
        try:
            run(["pip", "install", module_name], check=True)
            print(f"\n[?] The {module_name} module was successfully installed.\n")
            sleep(0.5)
            clear()
            
        except:
            raise ImportError(f"Installation of the '{module_name}' failed")
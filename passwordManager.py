### \author     @anoraktheomniscient
### \project    password-manager

if __name__ == "__main__":
    
    try:
        import argparse
        from src.App import App
        from argparse import ArgumentError
    
    except ImportError as e:
        print(f"[!] ImportError: {e}")
        exit(1)
    
    except Exception as e:
        print(f"[!] Error: {e}")
        exit(1)
    
    try:
        parser = argparse.ArgumentParser(exit_on_error=True)
        
        parser.add_argument('-i', metavar='input',type=str, help='Enter the input file path')
        parser.add_argument('-p', metavar='password',type=str, help='Enter the file password')
        
        args = parser.parse_args()
        filePath = args.i
        password= args.p
    
    except ArgumentError as e:
        print(f"[!] ArgumentError: {e}")
        exit(1)
    
    except Exception as e:
        print(f"[!] Error: {e}")
        exit(1)
    
    passwordManager = App(filePath=filePath, password=password)
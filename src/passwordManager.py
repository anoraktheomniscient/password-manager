### \author     @anoraktheomniscient
### \project    password-manager

if __name__ == "__main__":
    
    try:
        import argparse
        from App import App
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
        
        args = parser.parse_args()
        filePath = args.i
    
    except ArgumentError as e:
        print(f"[!] ArgumentError: {e}")
        exit(1)
    
    except Exception as e:
        print(f"[!] Error: {e}")
        exit(1)
    
    passwordManager = App(filePath=filePath, password="mypassword")
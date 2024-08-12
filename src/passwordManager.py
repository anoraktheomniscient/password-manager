### \author     @anoraktheomniscient
### \project    password-manager

if __name__ == "__main__":
    
    try:
        import argparse
        from App import App
    
    except ImportError as e:
        print(f"[!] ImportError: {e}")
        exit(1)
    
    except Exception as e:
        print(f"[!] Error: {e}")
        exit(1)
    
    try:
        parser = argparse.ArgumentParser(exit_on_error=True)
        
        parser.add_argument('-i', metavar='input',type=str, help='Enter the input file')
        
        args = parser.parse_args()
        inputFile = args.i
    
    except Exception as e:
        print(f"[!] Error: {e}")
        exit(1)
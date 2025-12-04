from black_mirror.core import BlackMirror
import json

def main():
    print("Initializing Black Mirror...")
    bm = BlackMirror()
    
    target = "support@github.com"
    print(f"Looking up: {target}")
    
    # Direct API call
    result = bm.lookup("email", target)
    
    print("\nResult:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

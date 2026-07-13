import os
import time
import sys

Fast_File_Finder = """
 (       *    (        *    (    (   (           (    (       ) (  *      (     
 )\ )   (     )\ ) *   )    )\ ) )\ ))\ ) *      )\ ) )\ ) ( /( )\ )  *   )\ )  
(()/(   )\  (()/(` )  /(   (()/((()/(()/( (     (()/((()/( )\()|()/(  (  (()/(  
 /(_)|(((_)(  /(_))( )(_))__ /(_))/(_))(_)))\ ___ /(_))/(_)|(_)\ /(_)) )\  /(_)) 
(_))_|)\ _ )\(_)) (_(_())___(_))_(_))(_)) ((_)___(_))_(_))  _((_|_))_ ((_)(_))   
| |_  (_)_\(_) __||_   _|   | |_ |_ _| |  | __|  | |_ |_ _|| \| ||   \| __| _ \  
| __|  / _ \ \__ \  | |     | __| | || |__| _|   | __| | | | .` || |) | _||   /  
|_|   /_/ \_\|___/  |_|     |_|  |___|____|___|  |_|  |___||_|\_||___/|___|_|_\  
                                                                                 """
print(Fast_File_Finder + "\n\n")

print("Designed to find files/folders on your system :^)")

# Specify the name you're looking for as well as the directory
user_response = input("Input File or Folder Name (Include Item Name With Any Extensions):" "\n")
start_directory = input("\n"r"Starting Directory? (default is root C:\\)""\n") or "C:\\"
item_name = user_response 

# Animated Loading Function
def animated_message(message, duration=3):
    print("\n\n"+message, end="")
    for _ in range(duration * 3):
        for char in "|/-\\":
            sys.stdout.write(f"\r{message} {char}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r" + " " * (len(message)+2), end="\r")

# Item Finding Function
def find_item(item_name, start_directory):
    animated_message("Finding Item...")
    found = False
    for root, dirs, files in os.walk(start_directory):
        # Check for folders
        if item_name in dirs:
            print(f"Found folder: {os.path.join(root, item_name)}")
            found = True
            return os.path.join(root, item_name)
        # Check for Files
        elif item_name in files:
            print(f"Found File: {os.path.join(root, item_name)}")
            found = True
            return os.path.join(root, item_name)
    if not found:
        print(f"\nItem '{item_name}' not found.")
    return None

# Runs the search
found_folder = find_item(item_name, start_directory)
from modules.reverse_shells import reverse_shells
from modules.shell_stabilizer import shell_stabilizer
from modules.linux_privesc import linux_privesc
from modules.windows_privesc import windows_privesc
from modules.active_directory import active_directory
from modules.web_payloads import web_payloads

def banner():
    print("""
 ██████╗ ███████╗███████╗███████╗███████╗
██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██║   ██║█████╗  █████╗  █████╗  █████╗  
██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
╚██████╔╝██║     ██║     ██║     ███████╗
 ╚═════╝ ╚═╝     ╚═╝     ╚═╝     ╚══════╝

        OffsecToolkit
  Offensive Security Utility
      Created by Raszzy
""")

def menu():
    print("""
[1] Reverse Shell Generator
[2] Shell Stabilization
[3] Linux Privilege Escalation
[4] Windows Privilege Escalation
[5] Active Directory Enumeration
[6] Web Exploitation Payloads
[0] Exit
""")

def main():
    banner()
    while True:
        menu()
        choice = input("offsectoolkit > ")

        if choice == "1":
            reverse_shells()
        elif choice == "2":
            shell_stabilizer()
        elif choice == "3":
            linux_privesc()
        elif choice == "4":
            windows_privesc()
        elif choice == "5":
            active_directory()
        elif choice == "6":
            web_payloads()
        elif choice == "0":
            print("Happy hacking 👋")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

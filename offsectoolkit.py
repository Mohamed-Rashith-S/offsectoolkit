#!/usr/bin/env python3
import sys
import os

from modules.reverse_shells import reverse_shells
from modules.shell_stabilizer import shell_stabilizer
from modules.linux_privesc import linux_privesc
from modules.windows_privesc import windows_privesc
from modules.active_directory import active_directory
from modules.web_payloads import web_payloads
from modules.gtfobins import gtfobins_helper

# ===== COLORS =====
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(CYAN + r"""
 ██████╗ ███████╗███████╗███████╗███████╗
██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██║   ██║█████╗  █████╗  █████╗  █████╗  
██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
╚██████╔╝██║     ██║     ██║     ███████╗
 ╚═════╝ ╚═╝     ╚═╝     ╚═╝     ╚══════╝
""" + RESET)

    print(GREEN + "        OffsecToolkit")
    print("  Offensive Security Utility")
    print("      Created by Raszzy\n" + RESET)

def menu():
    print(CYAN + """
[1] Reverse Shell Generator
[2] Shell Stabilization
[3] Linux Privilege Escalation
[4] Windows Privilege Escalation
[5] Active Directory Enumeration
[6] Web Exploitation Payloads
[7] GTFOBins Helper
[0] Exit
""" + RESET)

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input("offsectoolkit > ").strip()

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
        elif choice == "7":
            gtfobins_helper()
        elif choice == "0":
            print(GREEN + "Happy hacking 👋" + RESET)
            sys.exit()
        else:
            input(RED + "Invalid option. Press Enter..." + RESET)

if __name__ == "__main__":
    main()

def windows_privesc():
    print("""
=== Windows Privilege Escalation ===

[Basic]
whoami
whoami /priv
systeminfo

[Users]
net user
net localgroup administrators

[Services]
sc query
wmic service get name,displayname,pathname,startmode

[Network]
ipconfig /all
netstat -ano

[WinPEAS]
winpeas.exe
""")
    input("Press Enter to return...")

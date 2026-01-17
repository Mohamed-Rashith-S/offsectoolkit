def active_directory():
    print("""
=== Active Directory Enumeration ===

[Import PowerView]
Import-Module .\\PowerView.ps1

[Domain]
Get-NetDomain
Get-NetDomainController

[Users]
Get-NetUser
Get-NetUser -SPN

[Groups]
Get-NetGroup
Get-NetGroupMember "Domain Admins"

[Computers]
Get-NetComputer

[ACL Abuse]
Find-InterestingDomainAcl

[BloodHound]
Invoke-BloodHound -CollectionMethod All
""")
    input("Press Enter to return...")

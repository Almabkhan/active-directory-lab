# Privilege Escalation Checks
Write-Host "PrivEsc Checks" -ForegroundColor Green
Write-Host "=============="

$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
Write-Host "`nCurrent User: $($currentUser.Name)"

Write-Host "`n[+] Checking complete!"
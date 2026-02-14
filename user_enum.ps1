# User Enumeration Script
Write-Host "AD User Enumeration" -ForegroundColor Green
Write-Host "==================="

$users = @("Administrator", "krbtgt", "sql_svc", "web_svc")
Write-Host "`nUsers found:"
foreach ($user in $users) {
    Write-Host "  • $user"
}
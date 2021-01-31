#$Hello = "Hello Powershell!"
#Write-Host($Hello)
function getIP{    
(get-netipaddress).ipv4address | Select-String "192*"}

write-host(getIP)
$Version = $Host.Version.Major
$IP = getIP
$Date = Get-Date
$Body = "This machine’s IP is $IP. User is $env:username. Hostname is $env:computername.
Powershell version $Version. Today's date and time is $Date "

Write-Host($Body)
#Send-MailMessage -To "konemuc@gmail.com" -From "konemuc@gmail.com" -Subject "IT3038C Window's sysinfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)

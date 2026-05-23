$lines = Get-Content -Path "style.css"
for ($i = 425; $i -lt 445; $i++) {
    $line = $lines[$i]
    Write-Host "${i}: '$line'"
}

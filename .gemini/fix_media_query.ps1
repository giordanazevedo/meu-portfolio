$lines = Get-Content -Path "style.css"
if ($lines[436] -eq "}") {
    Write-Host "Found brace at index 436. Inserting closing query brace."
    $lines[436] = "}`r`n}"
    Set-Content -Path "style.css" -Value $lines
} else {
    Write-Host "Brace not found at index 436. Actual content: '$($lines[436])'"
}

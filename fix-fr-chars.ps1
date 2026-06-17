$files = Get-ChildItem -LiteralPath "F:\Raptureholidaysllpsite\travela-1.0.0\fr" -Filter "*.html"
$search = [char]::ConvertFromUtf32(0x00C3) + [char]::ConvertFromUtf32(0x0083) + [char]::ConvertFromUtf32(0x00C2) + [char]::ConvertFromUtf32(0x00A9)
$replace = [char]::ConvertFromUtf32(0x00E9)
foreach ($f in $files) {
    $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    if ($c.Contains($search)) {
        $new = $c.Replace($search, $replace)
        [System.IO.File]::WriteAllText($f.FullName, $new, (New-Object System.Text.UTF8Encoding $false))
        Write-Output "Fixed: $($f.Name)"
    } else {
        Write-Output "Clean: $($f.Name)"
    }
}
Write-Output "Done"

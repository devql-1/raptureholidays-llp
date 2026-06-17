$dir = "F:\Raptureholidaysllpsite\travela-1.0.0\fr"
$search = [byte[]](0xC3, 0x83, 0xC2, 0xA9)
$replace = [byte[]](0xC3, 0xA9)
$files = Get-ChildItem -LiteralPath $dir -Filter "*.html" | Sort-Object Name
foreach ($f in $files) {
    $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
    $count = 0
    $i = 0
    while ($i -le $bytes.Length - $search.Length) {
        $match = $true
        for ($j = 0; $j -lt $search.Length; $j++) {
            if ($bytes[$i + $j] -ne $search[$j]) { $match = $false; break }
        }
        if ($match) {
            $bytes = $bytes[0..($i-1)] + $replace + $bytes[($i + $search.Length)..($bytes.Length - 1)]
            $count++
            $i += $replace.Length
        } else {
            $i++
        }
    }
    if ($count -gt 0) {
        [System.IO.File]::WriteAllBytes($f.FullName, $bytes)
        Write-Output "$($f.Name): fixed $count"
    }
}
Write-Output "Done"

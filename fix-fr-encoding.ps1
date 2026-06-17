$dir = "F:\Raptureholidaysllpsite\travela-1.0.0\fr"
$files = Get-ChildItem -LiteralPath $dir -Filter "*.html"
$replacements = @{}
$replacements['>We are passionate travelers who turn ordinary trips into extraordinary memories. From hidden gems to iconic landmarks, we design experiences that match your pace, style, and dreams.<'] = '>Nous sommes des voyageurs passionnés qui transforment les voyages ordinaires en souvenirs extraordinaires. Des joyaux cachés aux monuments emblématiques, nous concevons des expériences qui correspondent à votre rythme, votre style et vos rêves.<'
$replacements['>Handpicked stays from boutique hotels to luxury resorts that fit your budget and style.<'] = '>Séjours sélectionnés, des hôtels boutique aux resorts de luxe qui correspondent à votre budget et à votre style.<'
$replacements['>Local experts who turn sightseeing into stories and make every stop feel personal.<'] = '>Des experts locaux qui transforment les visites en histoires et rendent chaque arrêt personnel.<'
$replacements['>Premium services crafted to make every trip smooth, safe, and unforgettable.<'] = '>Services premium conçus pour rendre chaque voyage fluide, sûr et inoubliable.<'
$replacements['>Best fares, flexible dates, and exclusive airline partnerships for smooth departures.<'] = '>Meilleurs tarifs, dates flexibles et partenariats exclusifs avec des compagnies aériennes pour des départs fluides.<'
$replacements['>Comprehensive coverage so you can travel with confidence and total peace of mind.<'] = '>Couverture complète pour voyager en toute confiance et en toute sérénité.<'
$replacements['>Scenic routes, comfort stays, and flexible itineraries for road lovers.<'] = '>Paysages magnifiques, séjours confortables et itinéraires flexibles pour les amateurs de route.<'
$replacements['>Kid-friendly destinations, safe stays, and happy memories.<'] = '>Destinations adaptées aux enfants, séjours sûrs et souvenirs heureux.<'
$replacements['>Quick weekend getaways with handpicked stays and local experiences.<'] = '>Des escapades rapides du week-end avec des séjours soigneusement sélectionnés et des expériences locales.<'
$replacements['>Relaxing holiday packages designed for families and couples.<'] = '>Forfaits de vacances relaxants conçus pour les familles et les couples.<'
$replacements['>Smooth booking, amazing stay, and a trip we''ll never forget.<'] = '>Réservation facile, séjour exceptionnel et un voyage que nous n''oublierons jamais.<'

foreach ($f in $files) {
    $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $orig = $c
    foreach ($pair in $replacements.GetEnumerator()) {
        $c = $c.Replace($pair.Key, $pair.Value)
    }
    if ($c -ne $orig) {
        [System.IO.File]::WriteAllText($f.FullName, $c, (New-Object System.Text.UTF8Encoding $false))
        Write-Output "Updated $($f.Name)"
    }
}
Write-Output "Done"

$dir = 'F:\Raptureholidaysllpsite\travela-1.0.0\fr'
$files = Get-ChildItem -LiteralPath $dir -Filter '*.html'
foreach ($f in $files) {
    $txt = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $orig = $txt
    $txt = $txt -replace 'We are passionate travelers who turn ordinary trips into extraordinary memories\. From hidden gems to iconic landmarks, we design experiences that match your pace, style, and dreams\.', 'Nous sommes des voyageurs passionnes qui transforment les voyages ordinaires en souvenirs extraordinaires. Des joyaux caches aux monuments emblematiques, nous concevons des experiences qui correspondent a votre rythme, votre style et vos reves.'
    $txt = $txt -replace 'Handpicked stays from boutique hotels to luxury resorts that fit your budget and your style\.', 'Sejours selectionnes, des hotels boutique aux resorts de luxe qui correspondent a votre budget et a votre style.'
    $txt = $txt -replace 'Local experts who turn sightseeing into stories and make every stop feel personal\.', 'Des experts locaux qui transforment les visites en histoires et rendent chaque arret personnel.'
    $txt = $txt -replace 'Premium services crafted to make every trip smooth, safe, and unforgettable\.', 'Services premium concus pour rendre chaque voyage fluide, sur et inoubliable.'
    $txt = $txt -replace 'Handpicked national and international tours crafted for unforgettable experiences\.', 'Tours nationaux et internationaux selectionnes pour des experiences inoubliables.'
    $txt = $txt -replace 'Best fares, flexible dates, and exclusive airline partnerships for smooth departures\.', 'Meilleurs tarifs, dates flexibles et partenariats exclusifs avec des compagnies aeriennes pour des departs fluides.'
    $txt = $txt -replace 'Comprehensive coverage so you can travel with confidence and total peace of mind\.', 'Couverture complete pour voyager en toute confiance et en toute serenite.'
    $txt = $txt -replace 'Scenic routes, comfort stays, and flexible itineraries for road lovers\.', 'Paysages magnifiques, sejours confortables et itineraires flexibles pour les amateurs de route.'
    $txt = $txt -replace 'Kid-friendly destinations, safe stays, and happy memories\.', 'Destinations adaptees aux enfants, sejours srs et souvenirs heureux.'
    $txt = $txt -replace 'Quick weekend getaways with handpicked stays and local experiences\.', 'Des escapades rapides du week-end avec des sejours soigneusement selectionnes et des experiences locales.'
    $txt = $txt -replace 'Relaxing holiday packages designed for families and couples\.', 'Forfaits de vacances relaxants concus pour les familles et les couples.'
    $txt = $txt -replace 'Smooth booking, amazing stay, and a trip we will never forget\.', 'Reservation facile, sejour exceptionnel et un voyage que nous n\'oublierons jamais.'
    $txt = $txt -replace '\>Register\<', '>Inscription<'
    $txt = $txt -replace '\>Login\<', '>Connexion<'
    $txt = $txt -replace '\>Discover More\<', '>Decouvrir plus<'
    if ($txt -ne $orig) {
        [System.IO.File]::WriteAllText($f.FullName, $txt, (New-Object System.Text.UTF8Encoding $false))
        Write-Output "Updated $($f.Name)"
    } else {
        Write-Output "NoChange $($f.Name)"
    }
}
Write-Output 'Done'

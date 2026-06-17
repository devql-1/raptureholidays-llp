import os

fr_dir = r'F:\Raptureholidaysllpsite\travela-1.0.0\fr'
for fname in sorted(os.listdir(fr_dir)):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(fr_dir, fname)
    with open(path, 'rb') as f:
        raw = f.read()
    # decode as latin-1 to preserve exact bytes then fix double-encoded chars
    txt = raw.decode('latin-1')
    # Replace the double-encoded sequences at character level
    # These are the actual characters that appear when double-encoded UTF-8 is interpreted as UTF-8
    replacements = {
        '\u00c3\u00a9': '\u00e9',  # é
        '\u00e2\u00\u20ac\u2122': '\u00e9',  # another variant
    }
    txt = txt.replace('\u00c3\u00a9', '\u00e9')
    txt = txt.replace('\u00c3\u00a0', '\u00e0')
    txt = txt.replace('\u00c3\u00aa', '\u00ea')
    txt = txt.replace('\u00c3\u00f4', '\u00f4')
    txt = txt.replace('\u00c3\u00fb', '\u00fb')
    txt = txt.replace('\u00c3\u00ae', '\u00ee')
    txt = txt.replace('\u00c3\u00bb', '\u00bb')
    txt = txt.replace('\u00c3\u00e7', '\u00e7')
    
    # Now also fix English text
    txt = txt.replace('>Discover More<', '>Decouvrir plus<')
    txt = txt.replace('>Handpicked stays from boutique hotels to luxury resorts that fit your budget and your style.<', '>Sejours selectionnes, des hotels boutique aux resorts de luxe qui correspondent a votre budget et a votre style.<')
    txt = txt.replace('>Local experts who turn sightseeing into stories and make every stop feel personal.<', '>Des experts locaux qui transforment les visites en histoires et rendent chaque arret personnel.<')
    txt = txt.replace('>Premium services crafted to make every trip smooth, safe, and unforgettable.<', '>Services premium concus pour rendre chaque voyage fluide, sur et inoubliable.<')
    txt = txt.replace('>Handpicked national and international tours crafted for unforgettable experiences.<', '>Tours nationaux et internationaux selectionnes pour des experiences inoubliables.<')
    txt = txt.replace('>Best fares, flexible dates, and exclusive airline partnerships for smooth departures.<', '>Meilleurs tarifs, dates flexibles et partenariats exclusifs avec des compagnies aeriennes pour des departs fluides.<')
    txt = txt.replace('>Comprehensive coverage so you can travel with confidence and total peace of mind.<', '>Couverture complete pour voyager en toute confiance et en toute serenite.<')
    txt = txt.replace('>Scenic routes, comfort stays, and flexible itineraries for road lovers.<', '>Paysages magnifiques, sejours confortables et itineraires flexibles pour les amateurs de route.<')
    txt = txt.replace('>Kid-friendly destinations, safe stays, and happy memories.<', '>Destinations adaptees aux enfants, sejours srs et souvenirs heureux.<')
    txt = txt.replace('>Quick weekend getaways with handpicked stays and local experiences.<', '>Des escapades rapides du week-end avec des sejours soigneusement selectionnes et des experiences locales.<')
    txt = txt.replace('>Relaxing holiday packages designed for families and couples.<', '>Forfaits de vacances relaxants concus pour les familles et les couples.')
    txt = txt.replace('>Smooth booking, amazing stay, and a trip we will never forget.<', '>Reservation facile, sejour exceptionnel et un voyage que nous n\'oublierons jamais.')
    txt = txt.replace('>Register<', '>Inscription<')
    txt = txt.replace('>Login<', '>Connexion<')
    
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    
    # Verify fix
    verify = open(path, 'r', encoding='utf-8').read()
    if '\u00c3\u00a9' in verify or '\u00c3\u00a0' in verify:
        print(f'Still has encoding issues: {fname}')
    else:
        print(f'Fixed: {fname}')

print('Done')

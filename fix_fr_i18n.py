import os
import re

fr_dir = r'F:\Raptureholidaysllpsite\travela-1.0.0\fr'
for fname in sorted(os.listdir(fr_dir)):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(fr_dir, fname)
    with open(path, 'rb') as f:
        raw = f.read()
    txt = raw.decode('utf-8', errors='replace')

    # Normalize double-encoded accent sequences
    txt = txt.replace('\u00c3\u0083\u00c2\u00a9', '\u00e9')
    txt = txt.replace('\u00c3\u0083\u00c2\u00a0', '\u00e0')
    txt = txt.replace('\u00c3\u0083\u00c2\u00e2', '\u00ea')
    txt = txt.replace('\u00c3\u0083\u00c2\u00f4', '\u00f4')
    txt = txt.replace('\u00c3\u0083\u00c2\u00fb', '\u00fb')
    txt = txt.replace('\u00c3\u0083\u00c2\u00ee', '\u00ee')
    txt = txt.replace('\u00c3\u0083\u00c2\u00bb', '\u00bb')
    txt = txt.replace('\u00c3\u0083\u00c2\u00e7', '\u00e7')
    txt = txt.replace('\u00c3\u0083\u00c2\u00e0', '\u00e0')
    txt = txt.replace('\u00c3\u0083\u00c2\u00fa', '\u00fa')
    txt = txt.replace('\u00c3\u0083\u00c2\u00f9', '\u00f9')
    txt = txt.replace('\u00c3\u0083\u00c2\u00eb', '\u00eb')
    txt = txt.replace('\u00c3\u0083\u00c2\u00af', '\u00af')
    txt = txt.replace('\u00c3\u0083\u00c2\u00b4', '\u00b4')
    txt = txt.replace('\u00c3\u0083\u00c2\u00b6', '\u00b6')
    txt = txt.replace('\u00c3\u0083\u00c2\u00b8', '\u00b8')
    txt = txt.replace('\u00c3\u0083\u00c2', '\u00c2')

    repl = {
        '>Discover More<': '>Decouvrir plus<',
        '>Handpicked stays from boutique hotels to luxury resorts that fit your budget and your style.<': '>Sejours selectionnes, des hotels boutique aux resorts de luxe qui correspondent a votre budget et a votre style.<',
        '>Local experts who turn sightseeing into stories and make every stop feel personal.<': '>Des experts locaux qui transforment les visites en histoires et rendent chaque arret personnel.<',
        '>Premium services crafted to make every trip smooth, safe, and unforgettable.<': '>Services premium concus pour rendre chaque voyage fluide, sur et inoubliable.<',
        '>Handpicked national and international tours crafted for unforgettable experiences.<': '>Tours nationaux et internationaux selectionnes pour des experiences inoubliables.<',
        '>Best fares, flexible dates, and exclusive airline partnerships for smooth departures.<': '>Meilleurs tarifs, dates flexibles et partenariats exclusifs avec des compagnies aeriennes pour des departs fluides.<',
        '>Comprehensive coverage so you can travel with confidence and total peace of mind.<': '>Couverture complete pour voyager en toute confiance et en toute serenite.<',
        '>Scenic routes, comfort stays, and flexible itineraries for road lovers.<': '>Paysages magnifiques, sejours confortables et itineraires flexibles pour les amateurs de route.<',
        '>Kid-friendly destinations, safe stays, and happy memories.<': '>Destinations adaptees aux enfants, sejours srs et souvenirs heureux.<',
        '>Quick weekend getaways with handpicked stays and local experiences.<': '>Des escapades rapides du week-end avec des sejours soigneusement selectionnes et des experiences locales.<',
        '>Relaxing holiday packages designed for families and couples.<': '>Forfaits de vacances relaxants concus pour les familles et les couples.<',
        '>Smooth booking, amazing stay, and a trip we will never forget.<': '>Reservation facile, sejour exceptionnel et un voyage que nous n\'oublierons jamais.<',
    }
    changed = False
    for old, new in repl.items():
        if old in txt:
            txt = txt.replace(old, new)
            changed = True
    if changed or raw.decode('utf-8', errors='replace') != txt:
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(txt)
        print(f'Updated {fname}')
    else:
        print(f'Same {fname}')

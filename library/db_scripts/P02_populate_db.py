"""
DĖMESIO
šis kodas vykdomas per copy paste į Django Shell,
iškviečiamą terminale - python manage.py shell
"""


from library.models import Author, Book

authors = [
    Author.objects.create(first_name="Jonas", last_name="Biliūnas"),
    Author.objects.create(first_name="Antanas", last_name="Škėma"),
    Author.objects.create(first_name="Kristijonas", last_name="Donelaitis"),
    Author.objects.create(first_name="Maironis", last_name="Jonas"),
    Author.objects.create(first_name="Vincas", last_name="Mykolaitis-Putinas"),
]

books = [
    ("Liūdna pasaka", "Tragiška meilės istorija su istoriniu kontekstu.", "9786094444441", authors[0]),
    ("Vagis", "Kritika socialinei nelygybei ir neteisybei.", "9786094444442", authors[0]),
    ("Lazda", "Apie kaimo žmonių likimus ir moralines dilemas.", "9786094444443", authors[0]),

    ("Balta drobulė", "Modernistinis romanas apie asmeninę krizę ir kūrybą.", "9786095555551", authors[1]),
    ("Pabėgimas", "Siurrealistinis pasakojimas apie laisvės troškimą.", "9786095555552", authors[1]),

    ("Metai", "Poezijos kūrinys apie gamtos ciklą ir valstiečių gyvenimą.", "9786096666661", authors[2]),
    ("Pasakos", "Senųjų laikų pasakojimai su moralinėmis pamokomis.", "9786096666662", authors[2]),

    ("Pavasario balsai", "Poetinė knyga su stipriu tautiniu ir romantiniu prieskoniu.", "9786097777771", authors[3]),
    ("Jaunoji Lietuva", "Epinė poema apie patriotizmą ir tautos laisvę.", "9786097777772", authors[3]),

    ("Altorių šešėly", "Klasikinis romanas apie vidines kovas tarp kunigystės ir meilės.", "9786098888881", authors[4]),
    ("Vergas", "Psichologinis kūrinys apie žmogaus sielos laisvę ir kovą su ribotumais.", "9786098888882", authors[4]),
    ("Tylinti žemė", "Poetiškai parašyta apie žemę, žmones ir būtį.", "9786098888883", authors[4]),
]

for title, summary, isbn, author in books:
    Book.objects.create(title=title, summary=summary, isbn=isbn, author=author)

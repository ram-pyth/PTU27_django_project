from django.db import models
from django.contrib.auth.models import User
import uuid
import PIL


class Author(models.Model):
    """
    Autorių lentelės klasė
    reprezentuojanti vieną autorių
    """
    first_name = models.CharField('Vardas', max_length=50)
    last_name = models.CharField('Pavardė', max_length=50)
    description = models.TextField('Aprašymas', max_length=2000, default='biografija ir tt..')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def display_books(self):
        """
        book_set - django automatiškai
        kuriamas relationship į vaikinės
        lentelės susietas eilutes vienai
        knygai
        """
        res = ', '.join(elem.title for elem in self.book_set.all()[:3])
        return res

    class Meta:
        """
        Globalūs nuostatai Author modelio
        lentelei.
        ordering - rikiavimas
        """
        ordering = ('last_name', 'first_name')


class Genre(models.Model):
    """
    Žanrų lentelė, bus prijungta
    many-to-many su Book
    help_text - admino svetainėje
    rodomas pagalbos tekstas prie šio lauko
    """
    name = models.CharField('Žanras', max_length=15, help_text="Įveskite knygos žanrus")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Žanras'
        verbose_name_plural = 'Žanrai'


class Book(models.Model):
    """
    Viena knyga, autoriai turi ne po vieną
    todėl čia apsirašysim Foreign Key
    """
    title = models.CharField('Pavadinimas', max_length=100)
    summary = models.TextField('Aprašymas', max_length=1300)
    isbn = models.CharField('ISBN', max_length=13)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    cover = models.ImageField('Viršelis', upload_to='covers', null=True, blank=True)

    def display_genres(self):
        res = ', '.join(elem.name for elem in self.genres.all()[:3])
        return res

    def __str__(self):
        return f"{self.title}"


class BookInstance(models.Model):
    """
    Knygos konkretus egzempliorius išduodamas
    skaitytojui. id sudarysime uuid tipo
    pvz db195443-731e-4da7-9160-32928854fd87
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_back = models.DateField('Bus prieinama', null=True, blank=True)  # blank - dirba su Django forms
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # statusų rinkinys, (statuso kodas, pilnas statuso pavadinimas)
    LOAN_STATUS = (
        ('a', 'Administruojamas'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota')
    )

    # pats lentelės stulpelis, kuris naudos statusų rinkinį
    status = models.CharField('Statusas',
                              max_length=1,
                              choices=LOAN_STATUS,
                              default='a',
                              blank=True,
                              help_text='Knygos egzemplioriaus statusas')

    def __str__(self):
        return f'{self.id} {self.status} {self.due_back} {self.book} {self.book.author}'

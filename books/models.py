from django.db import models

# kitoblar uchun modellar. kitoblar haqidagi ma'lumotlar, janrlari, mualliflari bo'yicha tartiblanadi hammasi


class Books(models.Model):
    languages = [
        ('ru', 'Rus tili'),
        ('uz', 'O\'zbek tili'),
        ('ar', 'Arab tili'),
        ('tr', 'Turk tili'),
        ('eng', 'Ingliz  tili'),
    ]
    name = models.CharField(max_length=100) #kitob nomi
    author = models.CharField(max_length=100) # kitob muallifi
    publication_date = models.DateField(blank=True, null=True) #kitob nashr qilingan yil
    desc = models.TextField() #kitob haqida
    price = models.FloatField(default=0) #kitob narxi (sotib olgan yoki sotmoqchi bo'lgan narx)
    swap = models.BooleanField(default=True) #kitob almashish uchun ruxatmi? (odatiy holatda ruxsat beriladi)
    to_sell = models.BooleanField(default=False) #kitoblarni sotish uchun
    genres = models.ManyToManyField('Genre', null=True, blank=True) #kitob janrlari
    lang = models.CharField(max_length=100,choices=languages) #kitobning tilini tanlash


    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=150) #kitob janri

    def __str__(self) -> str:
        return self.genre


class Image(models.Model): 
    image = models.ImageField(upload_to='images/books')# bir kitob uchun bir nechta rasm yuklashni imkoni bo'lishi kerak. bu shunday qilish uchun model

    mymodel = models.ForeignKey(Books, related_name='imagesBooks', on_delete=models.CASCADE)


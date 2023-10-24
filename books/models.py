from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify  # new

from users.models import UserProfile
# kitoblar uchun modellar. kitoblar haqidagi ma'lumotlar, janrlari, mualliflari bo'yicha tartiblanadi hammasi


class Books(models.Model):
    languages = [
        ('Rus tili', 'Rus tili'),
        ('O\'zbek tili', 'O\'zbek tili'),
        ('Arab tili', 'Arab tili'),
        ('Turk tili', 'Turk tili'),
        ('Ingliz  tili', 'Ingliz  tili'),
    ]
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) #kitob nomi
    author = models.CharField(max_length=100) # kitob muallifi
    publication_date = models.DateField(blank=True, null=True) #kitob nashr qilingan yil
    desc = models.TextField() #kitob holati haqida
    price = models.FloatField(default=0) #kitob narxi (sotib olgan yoki sotmoqchi bo'lgan narx)
    swap = models.BooleanField(default=True) #kitob almashishq uchun ruxatmi? (odatiy holatda ruxsat beriladi)
    to_sell = models.BooleanField(default=False) #kitoblarni sotish uchun
    genres = models.ManyToManyField('Genre', verbose_name='Janrlar', blank=True) #kitob janrlari
    lang = models.CharField(max_length=100,choices=languages) #kitobning tilini tanlash
    created_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/books', blank=True, null=True)
    slug = models.SlugField(null=True) 
    location = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse("bookdetail", kwargs={"slug": self.slug}) 
  
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=150) #kitob janri

    def __str__(self):
        return self.genre


class Image(models.Model): 
    image = models.ImageField(upload_to='images/books')# bir kitob uchun bir nechta rasm yuklashni imkoni bo'lishi kerak. bu shunday qilish uchun model
    mymodel = models.ForeignKey(Books, related_name='imagesBooks', on_delete=models.CASCADE)



class Exchange(models.Model):
    borrower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='borrower') # kitobni kimga berilgani
    lender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='lender') # kitobni beruvchi
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookexchange') # kitob
    swap_time = models.DateTimeField(auto_now=True) # kitob yuborilgan vaqt
    sell = models.BooleanField(default=False)
    status = models.BooleanField(default=False) # kitob qaytarib berilgan bo'lsa false bo'ladi
    
    
    def __str__(self):
        return f"{self.lender.user.first_name} -- > {self.borrower.user.first_name}"


class BookLikes(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='booklikes')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userlikes')
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "user"], name="userLike"
            )
        ]
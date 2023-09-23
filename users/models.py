from django.db import models
from django.contrib.auth.models import User
from books.models import Books
# modellar. Asosan userlar uchun. userlar va boshqa applar uchun modellarni shu yerdan bog'lab qo'yamiz

# user modeli standart user modeli yordamida tuziladi
class Location(models.Model):
    regions = [
        ('andijan', 'Andijon viloyati'),
        ('bukhara', 'Buxoro viloyati'),
        ('fergana', 'Fargʻona viloyati'),
        ('jizzakh', 'Jizzax viloyati'),
        ('khorazm', 'Xorazm viloyati'),
        ('namangan', 'Namangan viloyati'),
        ('navoiy', 'Navoiy viloyati'),
        ('qashqadaryo', 'Qashqadaryo viloyati'),
        ('qoraqalpoq', 'Qoraqalpogʻiston Respublikasi'),
        ('samarkand', 'Samarqand viloyati'),
        ('sirdaryo', 'Sirdaryo viloyati'),
        ('surxondaryo', 'Surxondaryo viloyati'),
        ('tashkent', 'Toshkent viloyati'),
    ]
    region = models.CharField(max_length=100,choices=regions) 
    city = models.CharField(max_length=200,verbose_name='shahar nomini kiritishi kerak') # user o'zi yashaydigan shahar yoki tuman nomini kiritadi
    village =  models.CharField(max_length=200,verbose_name='qishloq yoki shahar nomini kiritishi kerak')

    def __str__(self) -> str:
        return self.region

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # asosiy malumotlarni user modelidan olamiz
    phone_number = models.CharField(max_length=20,blank=True) 
    blocklist = models.BooleanField(default=False) #userni blok qilish mumkin. admin qilishi mumkin faqat
    region = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()
    books = models.ManyToManyField(Books, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.get_full_name() 
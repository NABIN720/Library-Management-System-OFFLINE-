from django.db import models
from datetime import datetime, timedelta
import uuid

# Create your models here.

class Students(models.Model):
    roll_no = models.CharField(max_length=20,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    Guardian_name = models.CharField(max_length=100,help_text="Guardian Name")
    Email = models.EmailField(max_length=100,help_text="please enter your email")
    def __str__(self):
        return self.fullname
    
class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
        ('Biography', 'Biography'),
    ]

    id = models.UUIDField(primary_key=True, editable=False ,default= uuid.uuid4,help_text="Book unique id in the Library")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    ISBN = models.PositiveIntegerField(unique=True)
    genre = models.CharField(max_length=200,choices=GENRE_CHOICES)
    is_borrowed = models.BooleanField(default=False)
    book_no = models.PositiveIntegerField(null=True,help_text="Book numer for same kind of books")

    def __str__(self):
        return self.title

def get_expiry():
    return datetime.today() + timedelta(days=30)

class issue_book(models.Model):
    student = models.ForeignKey(Students, to_field='roll_no', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, to_field='id' ,on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=get_expiry())
    date_returned = models.DateField(null=True,blank=True)


    def __str__(self):
        return self.student.fullname



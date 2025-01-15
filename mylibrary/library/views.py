from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Students, Book, issue_book
from .forms import StudentsForm,BookForm,issue_bookForm
# Create your views here.

def index(request):
    return (render(request, 'main.html'))

def view_students(request):
    students = Students.objects.all()
    return render(request,'view_students.html',{'students':students})

def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_students')
    else:
        form = StudentsForm()
        
    return render(request, 'add_student.html',{'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html',{'form':form})

def view_books(request):
    books = Book.objects.all()
    return render(request,'view_books.html',{'books':books})

def add_book_issue(request):
    if request.method == 'POST':
        form = issue_bookForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            book_save = Book.objects.get(id = temp_form.book.id)
            book_save.is_borrowed=True
            book_save.save()
            form.save()
            form.save_m2m()
            return redirect('/book_issued')
    
    else:
        context={'form':issue_bookForm(), "bok":Book.objects.filter(is_borrowed=False),'students':Students.objects.all()}
        return render(request,'add_issue.html',context)
    
def book_issued(request):
    issue = issue_book.objects.all()
    return render(request, 'book_issued.html', {'issue': issue})


def dashboard(request,pk):
    # student = get_object_or_404(Students,id=pk)
    issue = issue_book.objects.filter(student_id= pk)
    bookl = []

    for i in issue:
        name = i.student.fullname
        id = i.id
        bookl.append(i.book)
        
        

    if not issue.exists():
        return render( request, 'dashboard.html',{'message':'no issues for this student till now'})
    
    print(bookl)    
    return render(request,'dashboard.html',locals())


def return_book(request,pk):
    print(pk)
    issue = issue_book.objects.get(pk=pk)
    issue.delete()
    return redirect('/view_students')

# def edit_issue(request,pk):
#     issue = issue_book.objects.get(id=pk)
#     form = issue_bookForm(instance=issue)
#     if request.method == 'POST':
#         form = issue_bookForm(request.POST,instance=issue)
#         if form.is_valid():
#             issue = form.save(commit=False)
#             form.save()
#             return redirect('book_issued')
#     return render(request,'add_issue.html',locals())
    

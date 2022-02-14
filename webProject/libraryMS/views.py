from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.

User = settings.AUTH_USER_MODEL

def index(request):
    context = {
        'books' : Book.objects.all(),
    }

    return render(request, 'pages/index.html', context)


def AdminSignUpView(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = AdminSignUpForm()
    return render(request, 'pages/signUp.html', {'form': form})



def StudentSignUpView(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = StudentSignUpForm()
    return render(request, 'pages/s_signUp.html', {'form': form})





def loginView(request):

    user = request.user
    if user.is_authenticated:
        return redirect('index')
    
    if request.POST:
        form = LoginForm(request.POST)
        
        if form.is_valid(): # to use attribute cleaned_data['email'] should call form.is_valid()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            #password = request.POST['password1']
            #print("email: "+email +"\npassword: "+password)

            user = authenticate(request, email=email, password=password) # error

            if user is not None:
                #print('iam logged in')
                login(request, user)
                return redirect('index')
            else:
                #print("n000000000")
                form = LoginForm()
                messages.error(request, 'invalid credintials!!') #in signup page

    
    else:
        #print('iam in else')
        form = LoginForm()
    

    return render(request, 'pages/login.html', {'loginform': form})




def logoutView(request):

    user = request.user
    if user.is_authenticated:
        logout(request)
    return redirect('index')


@login_required
def availableBooksView(request):
    user = request.user
    admin = Library_admin.objects.get(user=user)
    if user.is_student:
        return redirect('index')

    if request.method == 'POST':
        nform = NewBookForm(request.POST, request.FILES)
        if nform.is_valid():
            nform.save()

            addedBook = Book.objects.get(Title = nform.cleaned_data.get('Title'))
            admin.books.add(addedBook)
            return redirect('adminProfile')
    context = {
        'books' : admin.books.all(),
        'form' : NewBookForm()
    }

    return render(request, 'pages/adminProfile.html', context)


@login_required
def userProfileView(request):
    user = request.user
    student = Student.objects.get(user=user)
    context={
        'books': student.books.all()
    }
    return render(request, 'pages/userProfile.html', context)


@login_required
def userBorrow(request, id):
    user = request.user
    period = ''
    if not user.is_student:
        return redirect('index')
    else:
        myBooks = []
        if Student.objects.get(user=user):
            student = Student.objects.get(user=user) 

            newBook = Book.objects.get(isbn = id)
            if newBook and student:
                student.books.add(newBook)
                period = BorrowingPeriod.objects.create(student= student, book= newBook)
                period.save()
        
            myBooks = student.books
    context = {
        'books': myBooks.all(),
        'period': period 
    }


    return render(request, 'pages/userProfile.html', context)


@login_required
def deleteView(request, id):
    user = request.user
    if Student.objects.get(user=user):
        student = Student.objects.get(user=user)
        book = student.books.get(isbn = id)
        #book.delete()
        student.books.remove(book)
        return redirect('userProfile')
        
    return render(request, 'pages/index.html')


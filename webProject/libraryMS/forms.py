from django.contrib.auth import  authenticate
from django.db.models import fields
from django.db.models.constraints import UniqueConstraint
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.db import transaction

class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length= 30,
        initial= '',
        widget= forms.TextInput(attrs={'id': 'emailView', 'placeholder': 'Enter Email'})
    )

    username = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.TextInput(attrs={'id': 'userNameView', 'type':'text', 'placeholder': 'Enter Username'})
    )

    password1 = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.PasswordInput(attrs={'id': 'passView', 'type':'password', 'placeholder': 'Enter Password'})
    )

    password2 = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.PasswordInput(attrs={'id': 'confirmView', 'type':'password', 'placeholder': 'Confirm Password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields= ['email', 'username', 'password1', 'password2']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_library_admin = True
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        admin = Library_admin.objects.create(user=user)
        admin.save()
        return user

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qry = User.objects.filter(email__iexact=email)
        if qry.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


    def clean(self):
        super(AdminSignUpForm, self).clean()

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            self._errors['password2'] = self.error_class(["password doesn't match"])

        return self.cleaned_data


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length= 30,
        initial= '',
        widget= forms.TextInput(attrs={'id': 'emailView', 'placeholder': 'Enter Email'})
    )

    username = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.TextInput(attrs={'id': 'userNameView', 'type':'text', 'placeholder': 'Enter Username'})
    )

    password1 = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.PasswordInput(attrs={'id': 'passView', 'type':'password', 'placeholder': 'Enter Password'})
    )

    password2 = forms.CharField(
        max_length= 30,
        required= True,
        widget= forms.PasswordInput(attrs={'id': 'confirmView', 'type':'password', 'placeholder': 'Confirm Password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields= ['email', 'username', 'password1', 'password2']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qry = User.objects.filter(email__iexact=email)
        if qry.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


    def clean(self):
        super(StudentSignUpForm, self).clean()

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            self._errors['password2'] = self.error_class(["password doesn't match"])

        return self.cleaned_data


                                    
   


class LoginForm(forms.Form):

    email = forms.EmailField(widget= forms.TextInput(attrs={'id': 'login-view', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'login-view1', 'type':'password', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['email', 'password1']
    




class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'image', 'status', 'isbn']
        widgets={
            'isbn': forms.TextInput(attrs={'type':'text'}),
            'Title': forms.TextInput(attrs={'type':'text', 'placeholder': 'Enter Book Title'}),
            'Author': forms.TextInput(attrs={'type':'text', 'placeholder': 'Enter Author Name'}),
            'Price': forms.TextInput(attrs={'type':'text', 'placeholder': 'Enter Book Price'}),
            'image': forms.FileInput(),
            'status': forms.Select(attrs={'type':'text'}),
        }






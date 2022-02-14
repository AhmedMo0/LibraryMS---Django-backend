from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Library_admin)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BorrowingPeriod)


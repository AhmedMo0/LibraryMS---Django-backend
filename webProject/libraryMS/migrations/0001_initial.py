# Generated by Django 3.2.5 on 2022-02-14 07:01

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_library_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('password1', models.CharField(default='', max_length=30)),
                ('password2', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/users')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(default='', max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='ISBN')),
                ('Title', models.CharField(max_length=60, verbose_name='Title')),
                ('Author', models.CharField(blank=True, max_length=30, null=True)),
                ('Price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/books')),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], default='available', max_length=30)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Library_admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='libraryMS.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='libraryMS.user')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2022, 2, 21, 9, 1, 38, 472420))),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='libraryMS.book')),
            ],
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(('Price__gte', '0.01')), name='product_price_non_negative'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='student',
            name='books',
            field=models.ManyToManyField(to='libraryMS.Book'),
        ),
        migrations.AddField(
            model_name='library_admin',
            name='books',
            field=models.ManyToManyField(to='libraryMS.Book'),
        ),
        migrations.AddField(
            model_name='borrowingperiod',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='libraryMS.student'),
        ),
    ]

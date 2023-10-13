# Create your views here.
# user_management/views.py
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

from utils.decorators import student_required, staff_required, admin_required, editor_required
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            LogoutView.as_view()(request)
            return redirect('login')  # Redirect to the user's profile page or another page

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.user.is_authenticated:
        print(request.user.role)
        # Redirect authenticated users to a different page (e.g., the user's profile)
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Correct username and password, log in the user
            login(request, user)

            if user.role == 'student':
                return redirect('student')
            elif user.role == 'admin':
                return redirect('custom_admin')
            elif user.role == 'staff':
                return redirect('staff')
            elif user.role == 'editor':
                return redirect('editor')
            else:
                return redirect('profile')
        else:
            # Incorrect username or password
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')


@student_required
def student_view(request):
    # Assuming you want to pass user-specific data to the template
    return render(request, 'role_templates/student.html')


@staff_required
def staff_view(request):
    # Assuming you want to pass user-specific data to the template
    return render(request, 'role_templates/staff.html')


@admin_required
def admin_view(request):
    # Assuming you want to pass user-specific data to the template
    return render(request, 'role_templates/admin.html')


@editor_required
def editor_view(request):
    # Assuming you want to pass user-specific data to the template
    return render(request, 'role_templates/editor.html')


def profile(request):
    # Assuming you want to pass user-specific data to the template
    user = request.user  # Access the user object

    context = {
        'user': user,  # Pass the user object to the template
    }

    return render(request, 'registration/profile.html', context)


def custom_logout(request):
    # Perform the logout operation
    LogoutView.as_view()(request)

    # Redirect the user to the login page
    return redirect('login')

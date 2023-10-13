from functools import wraps

from django.shortcuts import render


def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'student':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'general/forbidden.html')

    return _wrapped_view


def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'staff':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'general/forbidden.html')

    return _wrapped_view


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'general/forbidden.html')

    return _wrapped_view


def editor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'editor':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'general/forbidden.html')

    return _wrapped_view

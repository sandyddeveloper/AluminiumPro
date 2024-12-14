from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(f"Attempting login for username: {username}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(f"User {username} authenticated successfully.")
            
            login(request, user)
            
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                return redirect('student_dashboard')  # Redirect to student dashboard
        else:
            print(f"Authentication failed for username: {username}")
            return HttpResponse('Invalid login credentials')
    
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'admin_dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'student_dashboard.html')

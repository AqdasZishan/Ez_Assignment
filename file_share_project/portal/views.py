from django.shortcuts import render, redirect
from .models import FileUpload

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        # Custom redirect logic based on the username
        if username.startswith('admin'):
            return redirect('boss_dashboard')  # Redirect to the custom Boss/Admin dashboard
        elif username.startswith('user'):
            return redirect('user_dashboard')  # Redirect to the user dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid username'})
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .models import FileUpload

# Boss (Admin) Dashboard - File Upload
def boss_dashboard(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        FileUpload.objects.create(file=uploaded_file)
    return render(request, 'boss_dashboard.html')


from .models import FileUpload

# User Dashboard - File List and Download
def user_dashboard(request):
    files = FileUpload.objects.all()  # Get all uploaded files by the admin
    return render(request, 'user_dashboard.html', {'files': files})

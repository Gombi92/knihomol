from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from UserLibrary.models import UserLibrary
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Šablona pro přihlášení

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Účet vytvořen! Nyní se můžete přihlásit.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_library(request):
    if request.user.is_authenticated:
        user = request.user  # Získej přihlášeného uživatele
        books_in_library = UserLibrary.objects.filter(user=user).select_related(
            'book')  # Získání všech knih, které vlastní uživatel

        context = {
            'books_in_library': books_in_library,
        }
        return render(request, 'user_library.html', context)
    else:
        return redirect('login')  # Přesměrování na přihlašovací stránku, pokud uživatel není přihlášen

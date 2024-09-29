from django.shortcuts import render
from UserLibrary.models import UserLibrary  # Naimportuj model UserLibrary


def user_library(request):
    # Získání přihlášeného uživatele
    user = request.user

    # Získání všech knih, které uživatel vlastní
    books_in_library = UserLibrary.objects.filter(user=user).select_related('book')

    # Přenesení seznamu knih do šablony
    context = {
        'books_in_library': books_in_library,
    }

    # Render šablony 'user_library.html' s předaným kontextem
    return render(request, 'user_library.html', context)

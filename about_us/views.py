from django.contrib.auth import get_user_model
from django.shortcuts import render


def about_us(request):
    context = {
        'members': get_user_model().objects.exclude(first_name='').exclude(last_name='')
    }
    return render(request, 'about_us.html', context)

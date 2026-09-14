import random
from datetime import date
from django.shortcuts import render, redirect
from .forms import PlaceForm

DEFAULT_PLACES = [
    {
        'id': 1,
        'title': 'ВДНГ',
        'description': 'Парк в якому знайдетуться розваги для всієї родини, від музеїв до атракціонів.',
        'place_type': 'Парк / Сквер',
        'location': 'м. Київ, ст. метро ВДНГ',
        'rating': 5,
        'created_at': '2026-09-14'
    },
    {
        'id': 2,
        'title': 'Експериментаріум',
        'description': 'На вас чекають захопливі експерименти, дивовижні відкриття, інтерактивні зали та незабутні враження!',
        'place_type': 'Музей / Виставка',
        'location': 'м. Київ, вулиця Борщагівська 154',
        'rating': 5,
        'created_at': '2026-09-14'
    }
]


def get_user_places(request):
    if 'places' not in request.session:
        request.session['places'] = DEFAULT_PLACES
    return request.session['places']


def weighted_random_place(places):
    weights = [place['rating'] for place in places]
    return random.choices(places, weights=weights, k=1)[0]


def home(request):
    return render(request, 'places/home.html', {'picked': False})


def random_place_view(request):
    places = get_user_places(request)
    random_place = weighted_random_place(places) if places else None
    return render(request, 'places/home.html', {'random_place': random_place, 'picked': True})


def place_list(request):
    places = get_user_places(request)
    return render(request, 'places/place_list.html', {'places': places})


def place_detail(request, place_id):
    places = get_user_places(request)
    place = next((p for p in places if p['id'] == place_id), None)
    return render(request, 'places/place_detail.html', {'place': place})


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = get_user_places(request)
            new_id = max((p['id'] for p in places), default=0) + 1
            new_place = {
                'id': new_id,
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'place_type': form.cleaned_data['place_type'],
                'location': form.cleaned_data['location'],
                'rating': form.cleaned_data['rating'],
                'created_at': str(date.today())
            }
            places.append(new_place)
            request.session.modified = True
            return redirect('place_list')
    else:
        form = PlaceForm()

    return render(request, 'places/add_place.html', {'form': form})
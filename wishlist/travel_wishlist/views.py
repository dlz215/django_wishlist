from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.
def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST) # Create new NewPlaceForm from data on the page. Pass data from form to constructor.
        place = form.save() # Create new Place object (model) from the form data. NewPlaceForm is aware of the Place model.
        if form.is_valid():
            place.save()    # Save model to database
            return redirect('place_list')   # reloads home page

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # create new empty NewPlaceForm, send to template to be rendered
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def about(request):
    author = 'David'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

# Django will extract place_pk value from url (in urls.py) and pass to function
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk) # without error handling
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()

    return redirect('place_list')

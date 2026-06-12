from django.shortcuts import render, redirect
from .models import Room, Booking
from .forms import BookingForm
from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import BookingForm
from .models import Room


def room_list(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('room_list')  
    else:
        form = BookingForm()  

    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'form': form
    }
    return render(request, 'core/room_list.html', context)

def review_list(request):
    reviews = Review.objects.order_by('-created_at')

    context = {
        'reviews': reviews
    }

    return render(request, 'core/review_list.html', context)


def review_detail(request, id):
    review = get_object_or_404(Review, id=id)

    context = {
        'review': review
    }

    return render(request, 'core/review_detail.html', context)

def create_booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = BookingForm()

    context = {
        'form': form
    }

    return render(request, 'core/booking_form.html', context)

def index(request):
    reviews = Review.objects.all()

    return render(
        request,
        'core/index.html',
        {'reviews': reviews}
    )

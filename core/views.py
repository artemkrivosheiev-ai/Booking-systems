from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Room, Booking, BookingStatus
from .forms import BookingForm
from .models import Review  


def room_list(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.guest_name = request.user.username if request.user.is_authenticated else "Гість"
            booking.save()
            messages.success(request, "Бронювання створено.")
            return redirect('core:room_list')
    else:
        form = BookingForm()

    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'form': form
    }
    return render(request, 'core/room_list.html', context)


def room_detail(request, pk: int):
    room = get_object_or_404(Room, pk=pk)
    form = None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.room = room
                booking.user = request.user
                booking.guest_name = request.user.username
                booking.save()
                messages.success(request, "Кімнату заброньовано.")
                return redirect("core:details", pk=room.pk)
        else:
            form = BookingForm(initial={"room": room})
    return render(request, "core/room_detail.html", {"room": room, "form": form})


def review_list(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'core/review_list.html', {'reviews': reviews})


def review_detail(request, id: int):
    review = get_object_or_404(Review, id=id)
    return render(request, 'core/review_detail.html', {'review': review})


def create_booking(request):
    # якщо хочеш окрему сторінку бронювання — можна залишити як є
    return redirect("core:room_list")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Обліковий запис створено. Ласкаво просимо!")
            return redirect("core:room_list")
    else:
        form = UserCreationForm()
    return render(request, "core/auth/register.html", {"form": form})


from django.contrib.auth.decorators import login_required

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "core/my_bookings.html", {"bookings": bookings})


def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.delete()
    messages.success(request, "Бронювання скасовано.")
    return redirect("core:my_bookings")


@login_required
def create_booking(request):
    room_id = request.GET.get("room_id")
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            return redirect("core:my_bookings")
    else:
        form = BookingForm()

    return render(request, "core/booking_form.html", {"form": form, "room": room})


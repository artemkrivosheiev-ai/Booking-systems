from django.db import models


class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Категорія кімнати"
        verbose_name_plural = "Категорії кімнат"

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField(unique=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"Кімната {self.number}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    class Meta:
        ordering = ['check_in']

    def __str__(self):
        return f"{self.guest_name} - {self.room}"
    
class Review(models.Model):
    guest_name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f"{self.guest_name} - {self.rating}/5"
    
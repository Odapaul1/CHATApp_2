from django.db import models

# Create your models here.

#	Create a model called Room:
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    def __str__(self):
        return self.room_name
    
# Create another model called Message:
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)

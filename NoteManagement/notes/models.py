from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class AudioRecording(models.Model):
    audio_file = models.FileField(upload_to='audio/')  # Save audio to 'media/audio/'
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio recording {self.id} - {self.created_at}"
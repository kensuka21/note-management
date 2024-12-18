from django.contrib.auth.models import Group, User
from rest_framework import serializers

from notes.models import Note, AudioRecording


class AudioRecordingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Modify the 'audio_file' field
        representation['audio_file'] = instance.audio_file.url.split("/")[-1:]
        return representation

    class Meta:
        model = AudioRecording
        fields = ['id', 'note_id', 'audio_file']

class NoteSerializer(serializers.ModelSerializer):
    audio_recordings = AudioRecordingSerializer(many=True, read_only=True, source='audiorecording_set')

    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'audio_recordings')


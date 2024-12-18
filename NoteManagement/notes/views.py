import os

from django.contrib.auth.models import Group, User
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from NoteManagement import settings
from notes.models import Note, AudioRecording
from notes.serializers import NoteSerializer, AudioRecordingSerializer




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):
    note = NoteSerializer(data=request.data)

    if note.is_valid():
        note.save()
        return Response(note.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_note_by_id(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_note(request, pk):
    note = Note.objects.get(pk=pk)
    data = NoteSerializer(instance=note, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if note:
        note.delete()

    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_audio(request, pk):
    note = Note.objects.get(pk=pk)
    recording = AudioRecording()
    recording.audio_file = request.data['audio_file']
    recording.note = note
    recording.note_id = note.id
    recording.save()

    data = AudioRecordingSerializer(instance=recording)

    return Response(data.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_audio(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'audio', file_name)

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
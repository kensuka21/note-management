
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.add_note, name='add-note'),
    path('all', views.get_notes, name='get-notes'),
    path('<int:pk>', views.get_note_by_id, name='get-notes-by-id'),
    path('<int:pk>/update', views.update_note, name='update-note'),
    path('<int:pk>/delete', views.delete_note, name='delete-note'),
    path('<int:pk>/upload_audio', views.upload_audio, name='upload_audio'),
    path('download_audio/<str:file_name>', views.download_audio, name='download_audio'),

]
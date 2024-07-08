from django.contrib.auth.views import LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path('create', views.NoteCreateView.as_view(), name='note_create'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
]

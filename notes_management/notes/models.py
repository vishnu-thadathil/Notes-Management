from django.contrib.auth import get_user_model
from django.db.models import (CASCADE, AutoField, CharField, ForeignKey, Model,
                              TextField)

User = get_user_model()


class Note(Model):
    note_id = AutoField(primary_key=True)
    title = CharField(max_length=200)
    body = TextField(null=True, blank=True)
    user = ForeignKey(User, on_delete=CASCADE)

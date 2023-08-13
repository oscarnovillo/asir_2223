from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from main.models import Question


class DeleteQuestion(DeleteView):
    model = Question
    success_url = reverse_lazy('main:index_poll')

from django.utils import timezone

from django.views import generic

from main.models import  Question

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class IndexView(PermissionRequiredMixin, generic.ListView):
    permission_required  = "main.view.question"
    permission_denied_message = "No tienes permisos para ver esta pagina"
    
    template_name = "main/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.db import transaction
from django.views import generic
from django.contrib.auth.decorators import login_required,permission_required
from main.models import Choice, Question
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.

@permission_required("main.can_eat_pizzas")
def index(request ) -> HttpResponse:
    return render(request,"index.html")

def index_poll(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"main/index.html",context, request)




class DetailView(generic.DetailView):
    model = Question
    template_name = "main/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "main/results.html"


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'main/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'main/logged_out.html'


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "main/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "main/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "main/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        with transaction.atomic():
            selected_choice.votes += 1
            selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("main:results", args=(question.id,)))
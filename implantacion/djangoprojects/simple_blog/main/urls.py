from django.urls import path
from main.views.views import index, detail, results, vote, index_poll
from main.views import views
from django.views.generic import TemplateView
from main.views.IndexView import IndexView
from main.views.SignupView import SignupView
from main.views.CreateQuestion import CreateQuestion
from main.views.DeleteQuestion import DeleteQuestion
from main.views.UpdateQuestion import UpdateQuestion

app_name = "main"

urlpatterns = [
    
    path('',views.index),
    # ex: /polls/5/
    path("polls/", IndexView.as_view(), name="index_poll"),
    path("polls/<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("polls/<int:question_id>/vote/", vote, name="vote"),
    path('polls/create/', CreateQuestion.as_view(),name='question-create'),
    path('polls/delete/<int:pk>', DeleteQuestion.as_view(),name='question-delete'),
    path('polls/update/<int:pk>/', UpdateQuestion.as_view(),name='question-update'),
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='registro',
        view=SignupView.as_view(),
        name='register'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=TemplateView.as_view(template_name='main/registerok.html'),
        name='registerok'
    ),
]
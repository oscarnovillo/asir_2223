# ..
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from main.models import Question

class CreateQuestion(CreateView):
    model = Question
    fields = "__all__"
    template_name = "main/form_question.html"
    success_url = reverse_lazy('main:index_poll')
    
    # change widget of datefiled pubdate
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['pub_date'].widget.attrs.update({'class': 'form-control'})
        form.fields['pub_date'].widget.input_type = 'date'
        
        return form

   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CreateQuestion,self).form_valid(form)

# other classes & functions



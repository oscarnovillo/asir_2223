from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from main.models import Question


class UpdateQuestion(UpdateView):
    model = Question
    success_url = reverse_lazy('main:index_poll')
    template_name = "main/update_question.html"
    fields = "__all__"
    
    # change widget of datefiled pubdate
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['pub_date'].widget.attrs.update({'class': 'form-control'})
        form.fields['pub_date'].widget.input_type = 'date'
        
        return form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was updated successfully.")
        return super(UpdateQuestion,self).form_valid(form)
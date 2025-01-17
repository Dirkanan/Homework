from django.shortcuts import render
from django.views.generic import TemplateView

def f_t(request):
    return render(request, 'second_task/fun.html')

class c_t(TemplateView):
    template_name = 'second_task/class.html'
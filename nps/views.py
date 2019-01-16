from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Answer, AnswerForm

def index(request):
	# TODO return template instead
	answer_list = Answer.objects.all()
	output = '<br/>'.join([a.answer_text for a in answer_list])
	return HttpResponse(output)
	
def submit_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # TODO save in database
            return HttpResponseRedirect('/thanks/')
    else:
        form = AnswerForm()
    return render(request, 'nps/nps_form.html', {'form': form})
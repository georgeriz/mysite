from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Answer, AnswerForm

from datetime import datetime

def index(request):
	# TODO return template instead
	answer_list = Answer.objects.all()
	output = '<br/>'.join([str(a) for a in answer_list])
	return HttpResponse(output)
	
def submit_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text = form.cleaned_data['answer_text']
            feedback_text = form.cleaned_data['feedback_text']
            answer_date = datetime.now()
            Answer(answer_text=answer_text, feedback_text=feedback_text, answer_date=answer_date).save()
            return HttpResponseRedirect('/nps/thanks/')
    else:
        form = AnswerForm()
    return render(request, 'nps/nps_form.html', {'form': form})
	
def thanks(request):
    return HttpResponse("thank you for answering")
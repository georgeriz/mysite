from django.http import HttpResponse

from .models import Answer

def index(request):
	# TODO return template instead
	answer_list = Answer.objects.all()
	output = '<br/>'.join([a.answer_text for a in answer_list])
	return HttpResponse(output)
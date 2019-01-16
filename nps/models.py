# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm

from django.db import models

class Answer(models.Model):
	# TODO answer_text should be an integer
	# and a restricted option
	answer_text = models.CharField(max_length=10)
	feedback_text = models.CharField(max_length=200)
	mail_text = models.CharField(max_length=200)
	user_text = models.CharField(max_length=200)
	answer_date = models.DateTimeField()
	
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'feedback_text']
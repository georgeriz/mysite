# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Answer(models.Model):
	# TODO answer_text should be an integer
	# and a restricted option
	answer_text = models.CharField(max_length=10)
	feedback_text = models.CharField(max_length=200)
	mail_text = models.CharField(max_length=200)
	user_text = models.CharField(max_length=200)
	answer_date = models.DateTimeField()
	
	def __str__(self):
		return ', '.join([self.answer_text, self.feedback_text, str(self.answer_date)])
	
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'feedback_text']
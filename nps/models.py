# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Answer(models.Model):
	choices = [
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
		(7,7),
		(8,8),
		(9,9),
		(10,10)]
	answer_text = models.IntegerField(choices=choices)
	feedback_text = models.CharField(max_length=200)
	mail_text = models.CharField(max_length=200)
	user_text = models.CharField(max_length=200)
	answer_date = models.DateTimeField()
	
	def __str__(self):
		return ', '.join([str(self.answer_text), self.feedback_text, str(self.answer_date)])
	
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'feedback_text']
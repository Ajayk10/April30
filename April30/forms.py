from django import forms
from .models import *

class AnswerForm1(forms.ModelForm):
	class  Meta:
		model = Answers1
		fields = '__all__'

class AnswerForm2(forms.ModelForm):
	class  Meta:
		model = Answers2
		fields = '__all__'

class AnswerForm3(forms.ModelForm):
	class  Meta:
		model = Answers3
		fields = '__all__'

class AnswerForm4(forms.ModelForm):
	class  Meta:
		model = Answers4
		fields = '__all__'

class AnswerForm5(forms.ModelForm):
	class  Meta:
		model = Answers5
		fields = '__all__'


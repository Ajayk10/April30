from django.shortcuts import render , redirect
from .models import *
from .forms import *

def home(request):
	return render(request, "home.html",{})

def I(request):
	if request.method == 'POST':
		form = AnswerForm1(request.POST or None)
		if form.is_valid():
			form.save()
			print("Passed")
			return redirect('II')
	return render(request, "I.html",{})

def II(request):
	if request.method == 'POST':
		form = AnswerForm2(request.POST or None)
		if form.is_valid():
			form.save()
			print("Passed")
			return redirect('III')
	return render(request, "II.html",{})

def III(request):
	if request.method == 'POST':
		form = AnswerForm3(request.POST or None)
		if form.is_valid():
			form.save()
			print("Passed")
			return redirect('IV')
	return render(request, "III.html",{})

def IV(request):
	if request.method == 'POST':
		form = AnswerForm4(request.POST or None)
		if form.is_valid():
			form.save()
			print("Passed")
			return redirect('V')
	return render(request, "IV.html",{})

def V(request):
	if request.method == 'POST':
		form = AnswerForm5(request.POST or None)
		if form.is_valid():
			form.save()
			print("Passed")
			return redirect('VI')
	return render(request, "V.html",{})

def VI(request):
	return render(request, "VI.html",{})

def VII(request):
	return render(request, "VII.html",{})

def VIII(request):
	return render(request, "VIII.html",{})

def IX(request):
	return render(request, "IX.html",{})

def X(request):
	return render(request, "X.html",{})

def record(request):
	data1 = Answers1.objects.all()
	data2 = Answers2.objects.all()
	data3 = Answers3.objects.all()
	data4 = Answers4.objects.all()
	data5 = Answers5.objects.all()
	context = {
				'data1':data1,'data2':data2,'data3':data3,'data4':data4,
				'data5':data5
				}
	return render(request, "record.html",context)
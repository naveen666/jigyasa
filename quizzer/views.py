from django.http import HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Category,Question,Choice
from django.http import HttpResponse
import random
score = [0]
done = {}
class IndexView(generic.ListView):
	template_name = 'quizzer/index.html'
	context_object_name = 'category_list'
	def get_queryset(self):
		score[0]=0
		done.clear()
		return Category.objects.order_by('category_text')
class QuestionView(generic.DetailView):
	model = Question
	template_name = 'quizzer/detail.html'

def startquiz(request,category_id):
	score = [0]
	print(category_id)
	question_list = Question.objects.filter(category_id=category_id)
	print(question_list)
	if question_list:
		for query in question_list:
			if not query.id in done:
					done[query.id]=1
					return render(request,'quizzer/detail.html',{'question':query,'score':score[0]})
	else:
		return render(request,'quizzer/noquestion.html',{'error_message':"No question added to this topic.",'score':0})
def quiz(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except :
		return render(request,'quizzer/detail.html',{'question':question,'error_message':"You didn't select a choice.",'score':score[0]})
	else:
		if selected_choice.iscorrect == True:
			categ = question.category.id
			question_list = sorted(Question.objects.filter(category_id=categ), key=lambda x: random.random())
			score [0] = score [0] + 10
			if score[0] >= 100:
				temporary = score [0] 
				score [0] = 0
				done.clear()
				return render(request,'quizzer/win.html',{'score':temporary})
			for query in question_list:
				if not query.id in done:
					done[query.id]=1
					return render(request,'quizzer/detail.html',{'question':query,'score':score[0]})
			temporary = score [0] 
			score [0] = 0
			done.clear()
			return render(request,'quizzer/win.html',{'score':temporary})
		else:
			temporary = score [0]
			score [0] = 0
			done.clear()
			selected_choice = question.choice_set.all()
			for choice in selected_choice:
				if choice.iscorrect:
					return render(request,'quizzer/gameover.html',{'correct':choice,'score':temporary})

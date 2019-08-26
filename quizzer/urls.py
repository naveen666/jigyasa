from django.urls import path
from . import views


app_name = 'quizzer'
urlpatterns=[
	path('',views.IndexView.as_view(),name='index'),
	path('<int:pk>/',views.QuestionView.as_view(),name='detail'),
	path('<int:category_id>/startquiz/',views.startquiz,name='startquiz'),
	path('noquestion/',views.startquiz,name='noquestion'),
	path('<int:question_id>/quiz/',views.quiz,name='quiz'),
]
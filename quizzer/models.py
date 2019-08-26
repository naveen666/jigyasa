from django.db import models

# Create your models here.
class Category(models.Model):
	def __str__(self):
		return self.category_text
	category_text = models.CharField(max_length=200)

class Question(models.Model):
	def __str__(self):
		return self.question_text
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	question_text = models.CharField(max_length=300)

class Choice(models.Model):
	def __str__(self):
		return self.choice_text;
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	iscorrect = models.BooleanField()
